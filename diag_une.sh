#!/bin/bash
set -e
REPO="$HOME/openroot"
echo '=== UNE REGISTRY DEPLOYMENT AUDIT ==='
echo "Repo: $REPO | Branch: $(git -C "$REPO" branch --show-current 2>/dev/null || echo 'no git')"
echo ''
echo '=== GIT STATUS (short) ==='
git -C "$REPO" status --short | cat
echo ''
echo '=== LAST 5 COMMITS ==='
git -C "$REPO" log --oneline -5
echo ''
echo '=== LOCAL une/ DIR ==='
if [ -d "$REPO/une" ]; then
  ls -la "$REPO/une"
  echo "JSONs present:"; ls "$REPO/une"/*.{json,jsonl} 2>/dev/null || echo "none"
else
  echo 'MISSING locally'
fi
echo ''
echo '=== LOCAL docs/axioms/ DIR ==='
if [ -d "$REPO/docs/axioms" ]; then
  ls -la "$REPO/docs/axioms"
else
  echo 'MISSING locally'
fi
echo ''
echo '=== GIT-TRACKED une/ + axioms/ ==='
git -C "$REPO" ls-files | grep -E '(^une/|^docs/axioms/)' || echo 'None tracked under une/ or docs/axioms/'
echo ''
echo '=== RECOMMENDED FIX (paste after review) ==='
echo 'If une/ exists locally with your symbol_registry.json + code_registry.jsonl + INDEX.md and AXIOM_REGISTRY.md ready:'
echo '  git -C $HOME/openroot add une/ docs/axioms/AXIOM_REGISTRY.md'
echo '  git -C $HOME/openroot commit -m "Deploy full UNE Registry: symbols+codes+index+AXIOM_REGISTRY (36 symbols, 7 codes, 40 axioms)"'
echo '  git -C $HOME/openroot push origin main'
echo ''
echo 'Post-push: re-browse the 3 links you gave. Then we run option 2 lookup test + wire ACRE ledger tagging (h003_ledger.log integration).'
echo 'This compounds: every future PoPW claim, thermal ledger entry, and axiom validator now has canonical UNE reference.'
