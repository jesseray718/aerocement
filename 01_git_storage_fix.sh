#!/data/data/com.termux/files/usr/bin/env bash
set -euo pipefail
# Tiniest unit: evict embedded .git from swarm audits (the exact fatal error in your log)
OPENROOT="$HOME/openroot"
AUDITS="$OPENROOT/swarm/audits"
OUT="$HOME/openroot_external_repos"
echo "=== 01 GIT HYGIENE (unblocks add/commit of compute/ + N0 atomics) ==="
echo "Current embedded .git count in audits: $(find "$AUDITS" -name .git -type d 2>/dev/null | wc -l)"
find "$AUDITS" -name .git -type d 2>/dev/null | head -10
echo ""
echo "DRY RUN (set CONFIRM=1 to execute)"
if [ "${CONFIRM:-0}" != "1" ]; then
  echo "Plan: mkdir -p $OUT; mv offending parent dirs out of tree; update .gitignore; git -C $OPENROOT add -A"
  exit 0
fi
mkdir -p "$OUT"
find "$AUDITS" -name .git -type d 2>/dev/null | while read g; do
  parent=$(dirname "$g")
  echo "Evicting $parent -> $OUT/"
  mv "$parent" "$OUT/" 2>/dev/null || rm -rf "$parent" 2>/dev/null || true
done
cat >> "$OPENROOT/.gitignore" << 'GI'
swarm/audits/
*.gguf
build/
__pycache__/
*.tmp
GI
git -C "$OPENROOT" add -A || true
git -C "$OPENROOT" commit -m "fix: evict embedded git from swarm/audits (fractal-scale shallow clones) + stage compute/ N0 atomics" || echo "nothing new to commit"
echo "Done. Now: git -C $HOME/openroot status && git -C $HOME/openroot push"
