#!/usr/bin/env python3
"""
Updated UNEClient with proper error handling
"""

import logging
import requests
from typing import Optional, Dict, Any

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UNEClient:
    def __init__(self, base_url="http://localhost:5001"):
        self.base_url = base_url
        logger.info(f"UNEClient initialized -> {self.base_url}")

    def get_health(self) -> bool:
        try:
            resp = requests.get(f"{self.base_url}/health", timeout=5)
            return resp.status_code == 200
        except Exception as e:
            logger.error(f"Health check failed: {e}")
            return False

    def resolve_entity(self, entity_id: str) -> Optional[Dict[str, Any]]:
        try:
            resp = requests.get(f"{self.base_url}/resolve/{entity_id}", timeout=5)
            return resp.json() if resp.status_code == 200 else None
        except Exception as e:
            logger.error(f"Resolve failed: {e}")
            return None

    def check_conflict(self, entity_id: str) -> Optional[Dict[str, Any]]:
        try:
            resp = requests.get(f"{self.base_url}/conflict/{entity_id}", timeout=5)
            return resp.json() if resp.status_code == 200 else None
        except Exception as e:
            logger.error(f"Conflict check failed: {e}")
            return None

    def validate_for_acre_claim(self, entity_id: str, claim_type: str = "physical_work") -> Dict[str, Any]:
        health = self.get_health()
        entity = self.resolve_entity(entity_id)
        conflict = self.check_conflict(entity_id)

        if not health:
            return {"approved": False, "reason": "UNE service unhealthy", "entity": None}
        if not entity:
            return {"approved": False, "reason": f"Entity {entity_id} not found", "entity": None}
        if conflict and conflict.get('has_conflict', False):
            return {"approved": False, "reason": f"Conflict: {conflict.get('details', 'Unknown')}", "entity": entity}

        return {"approved": True, "reason": "Valid claim", "entity": entity}

    def batch_resolve(self, entity_ids: list) -> Dict[str, Any]:
        return {eid: self.resolve_entity(eid) for eid in entity_ids}
