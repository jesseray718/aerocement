#!/bin/bash
echo "Setting up UNE system..."

# Create server if missing
if [ ! -f une_server.py ]; then
    cat > une_server.py << 'SERVER'
from flask import Flask, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Test data
entities = {
    'H003-thermal-node-01': {'id': 'H003-thermal-node-01', 'type': 'thermal_node'},
    'une:001': {'id': 'une:001', 'type': 'une_entity'}
}

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/resolve/<entity_id>')
def resolve(entity_id):
    return jsonify(entities.get(entity_id, {"error": "Not found"}))

@app.route('/conflict/<entity_id>')
def conflict(entity_id):
    return jsonify({"has_conflict": False, "details": "None"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
SERVER
fi

# Create client if missing
if [ ! -f une_client_updated.py ]; then
    cat > une_client_updated.py << 'CLIENT'
import requests

class UNEClient:
    def __init__(self):
        self.base_url = "http://localhost:5001"

    def get_health(self):
        try:
            return requests.get(f"{self.base_url}/health").json().get("status") == "healthy"
        except:
            return False

    def resolve_entity(self, entity_id):
        try:
            return requests.get(f"{self.base_url}/resolve/{entity_id}").json()
        except:
            return None

    def check_conflict(self, entity_id):
        try:
            return requests.get(f"{self.base_url}/conflict/{entity_id}").json()
        except:
            return None

    def validate_for_acre_claim(self, entity_id, claim_type):
        health = self.get_health()
        entity = self.resolve_entity(entity_id)
        conflict = self.check_conflict(entity_id)

        if not health:
            return {"approved": False, "reason": "Server unhealthy"}
        if not entity or "error" in entity:
            return {"approved": False, "reason": "Entity not found"}
        if conflict.get("has_conflict"):
            return {"approved": False, "reason": "Conflict detected"}

        return {"approved": True, "reason": "Valid claim", "entity": entity}
CLIENT
fi

# Start server
pkill -f une_server.py 2>/dev/null
python une_server.py &
sleep 2

# Test
curl -s http://localhost:5001/health
echo
echo "Setup complete!"
