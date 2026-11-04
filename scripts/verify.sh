#!/usr/bin/env bash
# Run real Lean/Lake commands, preserving all stdout, stderr, versions and exit codes.
set -Eeuo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPLAY_ROOT="${JACOBIAN_REPLAY_ROOT:-$ROOT/.replay}"
mkdir -p "$REPLAY_ROOT/receipts"
REPORT="$REPLAY_ROOT/receipts"
finish() {
  code=$?
  printf '%s\n' "$code" > "$REPORT/overall-exit.txt"
  date -u '+Finished UTC: %Y-%m-%dT%H:%M:%SZ' >> "$REPORT/environment.txt"
  echo "Jacobian replay exit code: $code"
}
trap finish EXIT
date -u '+Started UTC: %Y-%m-%dT%H:%M:%SZ' > "$REPORT/environment.txt"
uname -a >> "$REPORT/environment.txt"
for cmd in bash git curl unzip sha256sum python3 elan lean lake; do
  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "UNRESOLVED: missing executable $cmd" >&2
    exit 20
  fi
done

bash "$ROOT/scripts/fetch-source.sh" 2>&1 | tee "$REPORT/fetch-source.txt"
PROJECT="$REPLAY_ROOT/source/anc/lean"
cd "$PROJECT"
sha256sum lean-toolchain lakefile.toml lake-manifest.json KernelAudit.lean \
  DimensionTwoCounterexample/FinalTheorem.lean > "$REPORT/source-before.sha256"
lean --version 2>&1 | tee "$REPORT/lean-version.txt"
lake --version 2>&1 | tee "$REPORT/lake-version.txt"
elan --version 2>&1 | tee "$REPORT/elan-version.txt"
# Cache is optional. Never run `lake update`, never rewrite the author's dependency pins.
if [[ "${USE_MATHLIB_CACHE:-1}" == 1 ]]; then
  if lake exe cache get > "$REPORT/mathlib-cache.txt" 2>&1; then
     echo 'PASS: optional Mathlib cache downloaded' > "$REPORT/cache-status.txt"
  else
     echo 'UNRESOLVED: cache unavailable; compiling with pinned dependencies' > "$REPORT/cache-status.txt"
  fi
fi
set +e
lake build > "$REPORT/lake-build.txt" 2>&1
BUILD_RC=$?
set -e
printf 'lake build exit=%s\n' "$BUILD_RC" > "$REPORT/exit-codes.txt"
if [[ "$BUILD_RC" -ne 0 ]]; then
  echo "FAIL/UNRESOLVED: lake build exited $BUILD_RC; see raw logs" >&2
  exit "$BUILD_RC"
fi
for file in DimensionTwoCounterexample/GeometricBridge.lean \
  DimensionTwoCounterexample/FinalTheorem.lean KernelAudit.lean; do
  label="$(basename "$file" .lean)"
  set +e
  lake env lean "$file" > "$REPORT/$label.txt" 2>&1
  rc=$?
  set -e
  printf '%s exit=%s\n' "$file" "$rc" >> "$REPORT/exit-codes.txt"
  if [[ "$rc" -ne 0 ]]; then
    echo "FAIL: target Lean check $file exited $rc" >&2
    exit "$rc"
  fi
done
python3 "$ROOT/scripts/check-axioms.py" "$REPORT/KernelAudit.txt" \
  | tee "$REPORT/axiom-decision.txt"
sha256sum -c "$REPORT/source-before.sha256" \
  | tee "$REPORT/source-after-check.txt"
echo 'PASS: pinned author source built and kernel-axiom query passed the explicit policy.'
echo 'LIMITATION: no independent source-to-paper semantic verification or characteristic-zero result.'
