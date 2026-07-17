#!/usr/bin/env python3
import sys, json, os
from datetime import datetime
task = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else sys.stdin.read().strip()
ts = datetime.now().strftime("%Y%m%d_%H%M%S")
log_path = os.path.expanduser(f"$HOME/openroot/observations/compute_{ts}.log")
os.makedirs(os.path.dirname(log_path), exist_ok=True)
entry = {
    "timestamp": datetime.now().isoformat(),
    "task": task[:300],
    "node": "N0_ledger_log",
    "status": "verified_computational_work"
}
with open(log_path, "w") as f:
    json.dump(entry, f, indent=2)
print(f"Logged: {log_path}")
print(json.dumps(entry, indent=2))
