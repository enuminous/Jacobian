#!/usr/bin/env bash
# Fetch and authenticate Romy Mondello's unchanged author-hosted arXiv source bundle.
set -Eeuo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPLAY_ROOT="${JACOBIAN_REPLAY_ROOT:-$ROOT/.replay}"
AUTHOR_COMMIT=250457153d78427be7f2c5d1b65b1cdcd6658ca7
ZIP_GIT_BLOB=d09deacf37efecc3fc20d8d9480435e6d203c36e
LEAN_TOOLCHAIN=leanprover/lean4:v4.28.0
MATHLIB_SHA=8f9d9cff6bd728b17a24e163c9402775d9e6a365
SOURCE_URL="https://raw.githubusercontent.com/integrate-your-mind/integrate-your-mind.github.io/$AUTHOR_COMMIT/dimension-two-counterexample-arxiv.zip"

for cmd in curl git unzip sha256sum python3; do
  command -v "$cmd" >/dev/null 2>&1 || { echo "UNRESOLVED: missing $cmd" >&2; exit 20; }
done
mkdir -p "$REPLAY_ROOT" "$REPLAY_ROOT/receipts"
ZIP="$REPLAY_ROOT/dimension-two-counterexample-arxiv.zip"
printf '%s\n' "URL: $SOURCE_URL" "Git source commit: $AUTHOR_COMMIT" "Expected Git blob: $ZIP_GIT_BLOB" > "$REPLAY_ROOT/receipts/provenance.txt"

if [[ ! -f "$ZIP" ]]; then
  curl --fail --location --show-error --silent --retry 3 --connect-timeout 20 --max-time 180 \
    "$SOURCE_URL" --output "$ZIP"
fi
ACTUAL="$(git hash-object "$ZIP")"
printf 'Actual Git blob: %s\n' "$ACTUAL" | tee -a "$REPLAY_ROOT/receipts/provenance.txt"
if [[ "$ACTUAL" != "$ZIP_GIT_BLOB" ]]; then
  echo 'FAIL: original source archive differs from frozen author Git blob' >&2
  exit 21
fi
sha256sum "$ZIP" | tee -a "$REPLAY_ROOT/receipts/provenance.txt"

# Unzip only the verified author archive; never edit the source itself.
mkdir -p "$REPLAY_ROOT/source"
unzip -q -o "$ZIP" -d "$REPLAY_ROOT/source"
PROJECT="$REPLAY_ROOT/source/anc/lean"
for name in lean-toolchain lakefile.toml lake-manifest.json SOURCE_DIGESTS.sha256 \
  DimensionTwoCounterexample.lean KernelAudit.lean DimensionTwoCounterexample/FinalTheorem.lean; do
  [[ -f "$PROJECT/$name" ]] || { echo "FAIL: expected original source file absent: $name" >&2; exit 22; }
done

( cd "$PROJECT" && sha256sum -c SOURCE_DIGESTS.sha256 ) \
  > "$REPLAY_ROOT/receipts/source-digests.txt" 2>&1 || {
  cat "$REPLAY_ROOT/receipts/source-digests.txt" >&2
  echo 'FAIL: supplied original Lean source digests do not match' >&2
  exit 23
}
# Also check the whole author-distributed arXiv package manifest, if included.
if [[ -f "$REPLAY_ROOT/source/ARXIV_SOURCE_MANIFEST.sha256" ]]; then
 ( cd "$REPLAY_ROOT/source" && sha256sum -c ARXIV_SOURCE_MANIFEST.sha256 ) \
   > "$REPLAY_ROOT/receipts/archive-digests.txt" 2>&1 || {
   cat "$REPLAY_ROOT/receipts/archive-digests.txt" >&2
   echo 'FAIL: original arXiv package digests do not match' >&2
   exit 24
 }
fi

ACTUAL_TOOLCHAIN="$(tr -d '\r\n' < "$PROJECT/lean-toolchain")"
[[ "$ACTUAL_TOOLCHAIN" == "$LEAN_TOOLCHAIN" ]] || {
  echo "FAIL: Lean toolchain mismatch ($ACTUAL_TOOLCHAIN)" >&2; exit 25;
}
python3 - "$PROJECT/lake-manifest.json" "$MATHLIB_SHA" <<'PY'
import json, pathlib, sys
manifest=json.loads(pathlib.Path(sys.argv[1]).read_text())
packages=[p for p in manifest.get('packages',[]) if p.get('name')=='mathlib']
if len(packages)!=1 or packages[0].get('rev')!=sys.argv[2]:
    raise SystemExit('FAIL: locked Mathlib commit differs from frozen requirement')
print('PASS: frozen Mathlib revision',packages[0]['rev'])
PY
printf 'Pinned Lean: %s\nPinned Mathlib: %s\n' "$LEAN_TOOLCHAIN" "$MATHLIB_SHA" \
  | tee -a "$REPLAY_ROOT/receipts/provenance.txt"
printf 'PASS: Author source archive and Lean source digests validated.\n'
