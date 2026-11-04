#!/usr/bin/env python3
"""Parse #print axioms output conservatively; do not infer from a green build alone."""
import pathlib, re, sys
THEOREM = "DimensionTwoCounterexample.Final.fullCounterexample"
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
raw = pathlib.Path(sys.argv[1]).read_text(errors="replace")
if THEOREM not in raw:
    raise SystemExit("UNRESOLVED: terminal theorem not printed in raw Lean output")
# Lean typically formats: 'Namespace.theorem' depends on axioms: [a, b, ...].
match = re.search(r"\b(?:DimensionTwoCounterexample\.Final\.fullCounterexample)'?\s+depends on axioms:\s*\[([^\]]*)\]", raw)
if match:
    axioms = {s.strip() for s in match.group(1).split(",") if s.strip()}
else:
    if re.search(re.escape(THEOREM) + r"'?\s+does not depend on any axioms", raw):
        axioms = set()
    else:
        raise SystemExit("UNRESOLVED: unable to parse the actual #print axioms report")
print("Terminal theorem:", THEOREM)
print("Axioms from raw Lean output:", ", ".join(sorted(axioms)) or "none")
if not axioms <= ALLOWED:
    raise SystemExit("FAIL: unapproved axioms: " + ", ".join(sorted(axioms - ALLOWED)))
print("PASS: axiom output is within the explicit reported trust boundary")
