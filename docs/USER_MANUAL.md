# OpenRoot User Manual

## Core Loop (Floating Widget)
1. Copy text (task, note, receipt, AI response section).
2. Click floating widget (Tasker scene or notification button).
3. Script logs full input + system context to Markor.
4. Clean low-token output appears in clipboard.
5. Paste into any AI. Copy response → click widget again.

## Daily Tasks
- Log every business expense (`business` command + receipt note).
- Log personal 1% util moves.
- One AE-GFRC or recycling action.
- End-of-day `status`.

## Key Scripts (absolute paths)
- `/data/data/com.termux/files/home/openroot_tasker.sh` — floating widget processor + context injection.
- `/data/data/com.termux/files/home/openroot_finance_tracker.sh`
- `/data/data/com.termux/files/home/run_rampup.sh`

Never paste formatted text into Termux. Use absolute paths only. Widget is your single interface.
