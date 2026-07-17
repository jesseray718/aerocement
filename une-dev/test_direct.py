#!/usr/bin/env python3
import sys
import os

# Get current directory
print("Current directory:", os.getcwd())
print("Files present:", os.listdir('.'))

# Try to import
try:
    import une_client
    print("Successfully imported une_client")
    client = une_client.UNEClient()
    print("Client created:", client)
    print("Health check:", client.get_health())
except Exception as e:
    print("Error:", e)
    import traceback
    traceback.print_exc()
