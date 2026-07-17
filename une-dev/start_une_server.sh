#!/bin/bash
cd /data/data/com.termux/files/home/openroot
echo "Starting UNE Server on port 5001..."
python une_server.py &
sleep 2
echo "Server should be running. Checking..."
curl -s http://localhost:5001/health || echo "Server not responding"
