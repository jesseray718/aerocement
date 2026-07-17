#!/bin/bash
# OpenRoot Computational Flow Scheduler v2
# PoPW-enabled task router: expertise match → team assign → work_units log for ACRE
# Integrates: H-003 thermal, ACRE tokenomics, UNE, GitHub jesseray718/openroot

TEAMS_FILE="$HOME/openroot/swarm/teams.json"
TASKS_DIR="$HOME/openroot/swarm/tasks"
POW_LOG="$HOME/openroot/swarm/logs/pow_log.json"
mkdir -p "$(dirname "$POW_LOG")"

# Init PoPW log if missing
[ -f "$POW_LOG" ] || echo '[]' > "$POW_LOG"

# Load teams (array join fixed)
teams=$(jq -r 'to_entries[] | "\(.key):\(.value.expertise | join(","))"' "$TEAMS_FILE")

echo "=== OpenRoot Swarm Scheduler ==="
echo "Teams loaded. PoPW ledger: $POW_LOG"

for task_file in "$TASKS_DIR"/*.json; do
    [ -f "$task_file" ] || continue
    task_id=$(jq -r '.id' "$task_file")
    expertise_needed=$(jq -r '.expertise' "$task_file")
    task_name=$(jq -r '.name // "unnamed"' "$task_file")
    priority=$(jq -r '.priority // "medium"' "$task_file")

    echo "Scheduling $task_id [$priority] (needs: $expertise_needed)"

    assigned=false
    while IFS= read -r team_line; do
        team_name=$(echo "$team_line" | cut -d':' -f1)
        team_expertise=$(echo "$team_line" | cut -d':' -f2)
        if [[ "$team_expertise" == *"$expertise_needed"* ]]; then
            echo "→ Assigned to $team_name"
            # PoPW emission: base 1.0 work_unit * priority weight
            case "$priority" in
                high) wu=2.5 ;;
                medium) wu=1.0 ;;
                *) wu=0.5 ;;
            esac
            timestamp=$(date -Iseconds)
            jq --arg id "$task_id" --arg team "$team_name" --arg wu "$wu" --arg ts "$timestamp" \
               '. += [{"task_id":$id,"team":$team,"work_units":($wu|tonumber),"timestamp":$ts,"verified":false,"source":"scheduler_v2"}]' \
               "$POW_LOG" > "$POW_LOG.tmp" && mv "$POW_LOG.tmp" "$POW_LOG"
            assigned=true
            break
        fi
    done <<< "$teams"

    if [[ "$assigned" == false ]]; then
        echo "⚠ No suitable team for $task_id — consider new team or expertise expansion"
    fi
done

echo "=== PoPW ledger snapshot ==="
jq '. | length' "$POW_LOG" | xargs printf "Total tasks logged: %s\n"
echo "Next: aiq run on assigned tasks | git -C $HOME/openroot add swarm/ | commit for IPFS/Zenodo anchor"
