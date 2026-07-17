#!/usr/bin/env python3
import sys, json
from datetime import datetime
text = sys.stdin.read() if not sys.stdin.isatty() else " ".join(sys.argv[1:])
issues = []
eff = 0.92 if any(k in text.lower() for k in ["solar", "thermal", "passive", "capture"]) else 0.75
print(json.dumps({
    "timestamp": datetime.now().isoformat(),
    "issues": issues,
    "efficiency_score": eff,
    "fix": "ready for PoPW + H-003 integration" if eff > 0.85 else "increase solar thermal focus",
    "node": "N0_critique_output"
}, indent=2))
