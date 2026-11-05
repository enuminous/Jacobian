#!/usr/bin/env python3
"""Reproduce bounded audit controls; no Lean build or theorem proof is simulated."""
import argparse
import dataclasses
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = '1a4a649c77df4d869cc88d48d76a46fa489c3725'
THEOREM = 'DimensionTwoCounterexample.Final.fullCounterexample'

def run(args, **kw):
    p = subprocess.run(args, text=True, capture_output=True, **kw)
    return {'exit': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr}

def load_method(name):
    p = HERE / 'method' / (name + '.py')
    spec = importlib.util.spec_from_file_location('audit_' + name, p)
    m = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = m
    spec.loader.exec_module(m)
    return m

def polynomial_checks():
    # Sparse exact GF(2) polynomials: monomials present iff their coefficient is 1.
    class P:
        def __init__(self, terms=()): self.t = frozenset(terms)
        def __add__(a,b): return P(a.t ^ b.t)
        def __mul__(a,b):
            out=set()
            for u in a.t:
                for v in b.t:
                    w=tuple(x+y for x,y in zip(u,v))
                    if w in out: out.remove(w)
                    else: out.add(w)
            return P(out)
        def __pow__(a,n):
            out=P([(0,0)])
            for _ in range(n): out=out*a
            return out
        def d(a,i):
            out=[]
            for t in a.t:
                if t[i]%2:
                    u=list(t);u[i]-=1;out.append(tuple(u))
            return P(out)
        def at(a,x,y): return sum(x**i*y**j for i,j in a.t)%2
        def __eq__(a,b): return a.t==b.t
    one=P([(0,0)]); zero=P(); x=P([(1,0)]); y=P([(0,1)])
    p=x+x**2*y+x**4+x**6*y**2
    q=y+x**5+x**6*y+x**7*y**2+x**8*y**3
    r=one+x*y;u=one+x**3*r;w=r*u**2
    tests={
        'P_x':p.d(0)==one, 'P_y':p.d(1)==x**2,
        'Q_x':q.d(0)==x**4+x**6*y**2,
        'Q_y':q.d(1)==one+x**6+x**8*y**2,
        'jacobian_one':p.d(0)*q.d(1)+p.d(1)*q.d(0)==one,
        'P_compact':p==x*r*u, 'Q_compact':q==y+x**5*r**3,
        'recovery_x':x*q==one+w, 'recovery_r':p**2==x**2*r*w,
        'PQ_plus_P3':p*q+p**3==r*u+w**2,
        'hidden_cubic':w**3+w**2+(p*q+p**3)*w+p**3==zero,
        'derivative_at_hidden':w**2+p*q+p**3==r*u,
        'elimination':q**2*x**3+(p**3+p*q+one)*x+p==zero,
        'denominator_polynomials_nonzero':all(v!=zero for v in [x,q,r,u,w]),
        'origin':(p.at(0,0),q.at(0,0))==(0,0),
        'collision':all((p.at(a,b),q.at(a,b))==(0,1) for a,b in [(0,1),(1,0),(1,1)]),
        'negative_remove_y_detected':p.d(0)*(q+y).d(1)+p.d(1)*(q+y).d(0)!=one,
        'negative_characteristic_zero_detected':5*2-1*5!=1,
    }
    return {'status':'PASS' if all(tests.values()) else 'FAIL','checks':tests,
            'char_zero_determinant_at_1_0':5,
            'scope':'Exact polynomial calculations; no inference of generic degree from sampled fibers.'}

def strip_lean(s):
    out=[];i=0;depth=0;string=False
    while i<len(s):
        if depth:
            if s.startswith('/-',i):depth+=1;i+=2
            elif s.startswith('-/',i):depth-=1;i+=2
            else:out.append('\n' if s[i]=='\n' else ' ');i+=1
        elif string:
            if s[i]=='\\':i+=2
            elif s[i]=='"':string=False;i+=1
            else:out.append('\n' if s[i]=='\n' else ' ');i+=1
        elif s.startswith('/-',i):depth=1;i+=2;out.append(' ')
        elif s.startswith('--',i):
            j=s.find('\n',i);i=len(s) if j<0 else j
        elif s[i]=='"':string=True;i+=1;out.append(' ')
        else:out.append(s[i]);i+=1
    return ''.join(out)

def source_checks(project):
    sources=sorted(project.rglob('*.lean'))
    sources=[p for p in sources if '.lake' not in p.parts]
    markers=[];graph={};digests={};declarations=0
    for p in sources:
        rel=str(p.relative_to(project));s=strip_lean(p.read_text())
        digests[rel]=hashlib.sha256(p.read_bytes()).hexdigest()
        for m in re.finditer(r'\b(sorry|admit|axiom|unsafe|native_decide|implemented_by|extern)\b',s):
            markers.append({'file':rel,'line':s[:m.start()].count('\n')+1,'token':m.group()})
        declarations+=len(re.findall(r'\btheorem\s+',s))
        name=rel[:-5].replace('/','.')
        graph[name]=[m for line in re.findall(r'^import\s+([^\n]+)',s,re.M) for m in line.split() if m.startswith('DimensionTwoCounterexample')]
    visited=set();active=set();cycles=[]
    def visit(n):
        if n in active:cycles.append(n);return
        if n in visited:return
        active.add(n)
        for p in graph.get(n,[]):visit(p)
        active.remove(n);visited.add(n)
    for n in graph:visit(n)
    return {'status':'PASS' if not markers and not cycles else 'FAIL',
            'files':len(sources),'theorem_declarations':declarations,
            'markers':markers,'import_cycles':cycles,'local_import_graph':graph,'sha256':digests,
            'limitation':'Lexical and import screening only; transitive kernel axioms come from CI receipts.'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=HERE/'evidence'/'checks.json');args=ap.parse_args()
    pins=json.loads((HERE/'method/pins.json').read_text())
    for p in pins:
        b=(HERE/'method'/p['local']).read_bytes()
        got=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
        assert got==p.get('blob',p.get('git_blob_sha1')),p['local']
    project=ROOT/'.replay/source/anc/lean'
    if not project.exists():raise SystemExit('Run bash scripts/fetch-source.sh first.')
    normal=f"'{THEOREM}' depends on axioms: [propext, Classical.choice, Quot.sound]\n"
    cases=[
      ('allowed',normal,True),
      ('none',f"'{THEOREM}' does not depend on any axioms\n",True),
      ('sorry',f"'{THEOREM}' depends on axioms: [sorryAx]\n",False),
      ('custom',f"'{THEOREM}' depends on axioms: [User.assumption]\n",False),
      ('missing','',False),('truncated',f"'{THEOREM}' depends on axioms: [propext\n",False),
      ('wrong_name',normal.replace(THEOREM,'Other.theorem'),False),
      ('suffix_name',normal.replace(THEOREM,'Other.'+THEOREM),False),
      ('duplicate',normal+normal,False),
      ('contradictory',normal+f"'{THEOREM}' depends on axioms: [sorryAx]\n",False),
      ('reverse_contradictory',f"'{THEOREM}' depends on axioms: [sorryAx]\n"+normal,False),
      ('trailing_junk',normal.rstrip()+' unexpected trailing text\n',False),
    ]
    result={'baseline':BASE,'protocol_sha256':hashlib.sha256((HERE/'PROTOCOL.md').read_bytes()).hexdigest()}
    with tempfile.TemporaryDirectory(prefix='jacobian-zoo-') as td:
        td=Path(td);parser=td/'check-axioms.py'
        original=run(['git','show',BASE+':scripts/check-axioms.py'],cwd=ROOT)
        if original['exit']:raise SystemExit(original)
        parser.write_text(original['stdout'])
        def target(item):
            (td/'axioms.txt').write_text(item['text'])
            return run([sys.executable,str(parser),str(td/'axioms.txt')])
        trials=[]
        for name,raw,expected in cases:
            r=target({'text':raw})
            trials.append({'name':name,'input':raw,'expected_accept':expected,'accepted':r['exit']==0,
                           'correct':(r['exit']==0)==expected,**r})
        result['parser']={'status':'PASS' if all(r['correct'] for r in trials) else 'FAIL','cases':trials}
        weasel=load_method('weasel')
        invalid=[raw for _,raw,expected in cases if not expected]
        search=weasel.WeaselSearch(target,lambda r:float(r['exit']==0),{'text':invalid},{'text':''},max_changes=1)
        findings=[dataclasses.asdict(f) for f in search.search(top_n=20)]
        result['weasel']={'status':'FAIL' if findings else 'PASS','findings':findings,
                          'meaning':'FAIL is target rejection robustness; search successfully found witnesses.'}
        fetch=td/'harness/scripts/fetch-source.sh';fetch.parent.mkdir(parents=True)
        fetch.write_text(run(['git','show',BASE+':scripts/fetch-source.sh'],cwd=ROOT)['stdout'])
        replay=td/'seeded';replay.mkdir()
        shutil.copyfile(ROOT/'.replay/dimension-two-counterexample-arxiv.zip',replay/'dimension-two-counterexample-arxiv.zip')
        extra=replay/'source/anc/lean/AuditUnlisted.lean';extra.parent.mkdir(parents=True);extra.write_text('-- harmless stale-file sentinel\n')
        env=dict(os.environ,JACOBIAN_REPLAY_ROOT=str(replay))
        r=run(['bash',str(fetch)],env=env)
        result['stale_file']={'status':'FAIL' if r['exit']==0 and extra.exists() else 'PASS',
                              'extra_survived':extra.exists(),**r}
        (replay/'dimension-two-counterexample-arxiv.zip').write_bytes(b'corrupted archive control')
        r=run(['bash',str(fetch)],env=env)
        result['corrupt_archive']={'status':'PASS' if r['exit']==21 else 'FAIL',**r}
    result['polynomial']=polynomial_checks()
    result['source']=source_checks(project)
    # Real events: no fabricated historical build status, scores or author timestamps.
    elephant=load_method('elephant');mem=elephant.ElephantMemory()
    events=[('archive',0,'author archive', 'd09deacf37efecc3fc20d8d9480435e6d203c36e'),
            ('ci',1,'2026-11-04 completed replay','41917931365'),
            ('audit',2,'2026-11-05 audit of receipts',BASE)]
    # Deliberately insert out of order to exercise the upstream ordering operation.
    for eid,t,label,origin in reversed(events):mem.add_event(elephant.Event(eid,t,'audit',label,origin))
    ordered=[e.id for e in mem.history()]==[e[0] for e in events]
    provenance_ok=[e.provenance for e in mem.history()]==[e[3] for e in events]
    result['elephant']={'status':'PASS' if ordered and provenance_ok else 'FAIL','ordered_event_ids':[e.id for e in mem.history()],
        'provenance':[e.provenance for e in mem.history()],
        'scope':'Ordering and provenance preservation only; retention metric deliberately unused because it divides its own total by itself.'}
    salmon=load_method('salmon')
    nodes={k:salmon.Node(k,t) for k,t,_,_ in events}
    trace=salmon.SalmonTracer(nodes,[salmon.Edge('archive','ci',1),salmon.Edge('ci','audit',1)]).trace('audit')
    trace_ok=trace['origins']==[('archive',1.0)] and trace['max_depth']==2 and trace['unresolved_origin']==0
    result['salmon']={'status':'PASS' if trace_ok else 'FAIL','trace':trace,'scope':'Single-chain provenance bookkeeping; unit weights are edges, not evidential probabilities. One common source is not three independent proofs.'}
    circus=load_method('circus')
    cir={'animal':'CIRCUS','claim':'Unqualified independent certification of the complete paper',
         'pipeline':[{'stage':stage,'provenance_status':'documented'} for stage in ['definition','data_selection','labels','scoring','validation']],
         'dependencies':[{'materiality':'material','feedback':False}],
         'risks':[{'materiality':'material','status':'unresolved','id':'external literature equivalence and independent expert review'}],
         'independent_checks':[{'id':'local exact polynomial arithmetic','status':'passed','frozen':True,'independently_sourced':False}]}
    # Independently implemented arithmetic is not independent authorship or human review.
    result['circus']={'status':circus.decide(cir),'input':cir,
                      'scope':'Rejection of an overbroad certification claim, not rejection of the Lean theorem.'}
    monster=load_method('zoo-monster')
    mon={'animal':'MONSTER','preregistration':{'registered_before_outcomes':True,'protocol_id':'PROTOCOL.md parser controls'},
         'metric':{'direction':'higher_is_better','tolerance':1},'baseline':{'matched':True},
         'conditions':[{'id':r['name'],'registered':True,'status':'complete','candidate':int(r['correct']),'baseline':1} for r in trials],
         'failure_boundaries':[]}
    result['monster']={'status':monster.decide(mon),'input':mon,
                       'scope':'Frozen local test criteria, not prospective scientific preregistration. Baseline is explicit expected acceptance for the same cases.'}
    result['environment']={'lean_available':shutil.which('lean') is not None,'lake_available':shutil.which('lake') is not None,
                           'local_kernel_replay':'UNRESOLVED; use the preserved real GitHub Actions receipts'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v.get('status') for k,v in result.items() if isinstance(v,dict) and 'status' in v},indent=2))
    print('Known defects are reported in JSON; successful runner exit means the audit completed, not that the target passed.')

if __name__=='__main__':main()
