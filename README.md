# Jacobian — independent Lean 4.28.0 replay

**Status: reproducibility build under verification; not a second mathematical proof.**

A fresh, pinned, third-party reproduction harness for Romy Mondello's
*Dimension-Two Counterexample to the Separable Jacobian Conjecture in Characteristic Two*
([arXiv:2608.02634v1](https://arxiv.org/abs/2608.02634v1)).

The repository's goal is to compile the **author's unchanged Lean sources**, inspect the exact
fully qualified terminal theorem, print its real Lean kernel axioms, and preserve command logs
with honest `PASS / FAIL / UNRESOLVED` boundaries.

## Source of record (downloaded at build time)

- Author-hosted repository: [integrate-your-mind/integrate-your-mind.github.io](https://github.com/integrate-your-mind/integrate-your-mind.github.io)
- Frozen author repository commit: `250457153d78427be7f2c5d1b65b1cdcd6658ca7`
- Source archive at that commit: `dimension-two-counterexample-arxiv.zip`
- Git blob SHA-1 of that archive: `d09deacf37efecc3fc20d8d9480435e6d203c36e`
- Project root within the archive: `anc/lean/`
- Lean toolchain: `leanprover/lean4:v4.28.0`
- Locked Mathlib revision: `8f9d9cff6bd728b17a24e163c9402775d9e6a365`
- Terminal theorem: `DimensionTwoCounterexample.Final.fullCounterexample`
- Terminal axiom query: `anc/lean/KernelAudit.lean`

**The upstream proof is deliberately not rewritten, renamed, or relicensed here.** This
repository retrieves the immutable author-hosted source at execution time. The
formal proof and its ownership remain with their respective authors.

## Run the full build locally

Prerequisites: Linux/Ubuntu or compatible POSIX shell, Git, curl, unzip, sha256sum,
Python 3.10+, and outbound internet access. Install elan:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -o /tmp/elan-init.sh
sh /tmp/elan-init.sh -y --no-modify-path
export PATH="$HOME/.elan/bin:$PATH"
```

Then in this repository:

```bash
bash scripts/verify.sh
```

This automatically fetches the original source, verifies the source archive Git object
and its published SHA-256 digests, validates the toolchain and locked dependency
revision, attempts the pinned Mathlib cache without changing the manifest, runs a full
`lake build`, then executes `lake env lean KernelAudit.lean` and records the raw
axiom output. A nonzero step fails visibly; it is not promoted to certification.

For a manually hydrated source directory:

```bash
bash scripts/fetch-source.sh
cd .replay/anc/lean
lake build
lake env lean KernelAudit.lean
```

## GitHub Actions

Open [Actions](../../actions/workflows/lean-replay.yml) and select
**Pinned Lean / Lake / elan full replay**. The workflow also runs on pushes to
`main`. It uploads raw command outputs and exit codes even on failure. Repeated runs
must be evaluated against the frozen source and must not silently upgrade dependencies.

## What a green build would mean

A completed build and terminal check supports only that the imported theorem is
kernel-accepted under the recorded axioms and exact software environment. It is
**not** a proof that the paper's prose perfectly matches the formalization, a
characteristic-zero Jacobian counterexample, independent verification of mathematical
novelty, or experimental support for EFMW physics.

Independent verification is only claimed after an actual completed run with a pinned
source receipt, successful build, the terminal `#check` output, and literal
`#print axioms` evidence. See [VERIFICATION.md](VERIFICATION.md) for the
falsification gates.

## Provenance and attribution

Author of the mathematical construction and Lean proof: **Romy Mondello**.
Independent reproduction harness: **Monolithic LLC / Matthew Chenoweth Wright**.
Original source is fetched rather than mirrored because a public download link alone
does not establish a sublicense for the original work. Independent audit results
should distinguish faithful replay from semantic and priority claims.
