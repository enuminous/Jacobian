# Exact-source verification and risk boundary

## Target
- Mathematical author: Romy Mondello.
- Paper: https://arxiv.org/abs/2608.02634v1.
- Original author-hosted ZIP: https://github.com/integrate-your-mind/integrate-your-mind.github.io/blob/250457153d78427be7f2c5d1b65b1cdcd6658ca7/dimension-two-counterexample-arxiv.zip
- Immutable author-site Git commit: `250457153d78427be7f2c5d1b65b1cdcd6658ca7`.
- Source archive Git blob: `d09deacf37efecc3fc20d8d9480435e6d203c36e`.
- Lean: `leanprover/lean4:v4.28.0`.
- Mathlib: `8f9d9cff6bd728b17a24e163c9402775d9e6a365`.
- Terminal theorem: `DimensionTwoCounterexample.Final.fullCounterexample`.
- Terminal axiom query file: `KernelAudit.lean`.

## Evidence gates
| Gate | PASS | FAIL | UNRESOLVED |
| --- | --- | --- | --- |
| Source archive | Blob matches immutable author source | Hash differs | Download inaccessible |
| Archive SHA-256 manifest | Every listed source digest matches | Digest disagreement | Missing / malformed records |
| Toolchain and lock | Lean 4.28.0, exact locked Mathlib | Conflicting installed or checked revision | Environment cannot install/run |
| Complete library compilation | `lake build` exits zero | Reproducible source/proof error | Network, timeout, OOM, environment fault |
| Terminal proof | `lake env lean ...FinalTheorem.lean` exits zero | Kernel/typecheck failure | Could not execute |
| Axiom audit | `#print axioms` output parsed and subset of agreed allowlist | Unexpected axioms or `sorryAx` | Output absent or ambiguous |
| Statement correspondence | Independent proof statement vs published theorem match | Formal theorem materially weaker | Not yet audited |

Expected conventional Lean axiom allowlist: `propext`, `Classical.choice`, `Quot.sound`. The executable script reads the actual output; it does not infer an axiom list from a prior report.

## Nonclaims
No original mathematics is replaced, strengthened, newly discovered, or represented as independently peer-reviewed. Full Lean compilation alone cannot validate mathematical priority or the informal proof-to-formalization correspondence. This is a characteristic-two construction. No characteristic-zero Jacobian result or EFMW physical theory is certified.

The repository **does not mirror or relicense Romy's source**. It downloads the exact released file each run, then checks its identity. Author attribution remains unchanged.

## Reproduction

On Linux, install elan from Lean's official project; ensure `curl`, `git`, `unzip`, `sha256sum`, `python3` are available.

```bash
bash scripts/verify.sh
```

Inspect `.replay/receipts/`: full `lake-build.txt`, `KernelAudit.txt`, `axiom-decision.txt`, `exit-codes.txt`, source digests, toolchain versions and `overall-exit.txt`.

When run in GitHub Actions, download the run artifact `jacobian-lean-4-28-raw-receipts` even for red/yellow runs to classify the actual failure without guessing. The latest CI badge alone is insufficient to state the formalization is certified.
