# OpenRoot Operator’s Manual
## Jesse McMillen — Current Setup (July 2026)

### The One Rule
Never paste formatted text or markdown into the Termux shell.  
Use absolute paths only.  
The floating widget (or tasker button) is your single interface for everything.

### Core Daily Loop (Floating Widget)
1. Copy text, command, receipt note, task, or AI response section.
2. Click the floating widget / notification button.
3. The script runs:
   - Logs the full input + current system context (time, personal 1% track, business Mercury/DUNS/AE-GFRC/recycling/50-node status) to Markor.
   - Puts a clean, low-token version back in your clipboard.
4. Paste the clean version into any AI (Kai9000, Grok, etc.).
5. Copy the AI response → click widget again to continue the conversation with full context preserved.

This is how you talk to any AI without leaving the window and with almost zero token waste.

### Current Hardware & Apps
- Samsung Galaxy A15 + Termux + Shizuku + Alpine sandbox (via kai9000).
- Markor for all structured logging.
- Mercury business card (all work expenses).
- Personal credit: Kikoff cycling at strict 1% utilization for non-business wants only.
- Floating widget / Tasker scene or persistent notification button → runs `/data/data/com.termux/files/home/openroot_tasker.sh`.

### Key Scripts (absolute paths)
- `/data/data/com.termux/files/home/openroot_tasker.sh` — main floating widget processor + context injection.
- `/data/data/com.termux/files/home/openroot_finance_tracker.sh` — credit & business logging.
- `/data/data/com.termux/files/home/run_rampup.sh` — H-003 thermal ramp (use `ramp` alias after setup).

### Starting a New Context Window (any AI)
Option 1 (fastest): Copy this line and click the widget:
“New context window — full OpenRoot bootstrap status: zero-history personal 1% credit + Mercury/DUNS business + AE-GFRC + recycling node + 50-node cooperative vision active. Current tasks: [paste your current tasks here].”

Option 2: Create a small “context starter” file in Markor or photos, send/share it, then run it through the widget.

### Logging Everything (the habit that compounds)
Every money move, receipt, idea, AI response section, or task goes through the widget.  
Tag correctly:
- Personal consumption or credit building → `kikoff`, `personal`, or `util`
- Business / work-related → `business`, `concrete`, `recycling`, `node_scaling`

This creates the living PoPW work ledger and ACRE data layer.

### Vision (why we do this)
From true zero credit and cash-only life → personal credit at 1% util for comfort → business credit (Mercury + DUNS) for AE-GFRC production and recycling node → 50-node decentralized cooperative with rotating roles, equal profit/asset share, shared farm, 501c3 feedback, fractal AI per node, and community wealth recapture.

The widget + tasker + Markor is the universal nervous system that makes the whole thing run with least human effort.

### How to Update This Manual
1. Copy the section you want to change.
2. Click the floating widget.
3. Edit the file in Markor or with a text editor.
4. Run the widget again on the updated section so it stays in the living log.

### Current Known Gaps (as of today)
- Floating widget / Tasker scene not yet fully installed (plan to have someone set it up or do it yourself via Tasker floating scene pointing to the tasker script).
- Directories and documents partially created — finish with the mkdir + cat blocks in the setup guide.

Keep this file open in Markor. Read sections aloud when needed. Every time you use the widget you are training the system and building the coefficient.
