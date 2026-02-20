#!/bin/bash

# Test script for OctoFit Tracker API endpoints
# Usage: bash test_api.sh

# Get the CODESPACE_NAME environment variable
CODESPACE_NAME=${CODESPACE_NAME:-"localhost"}

# Set the base URL
if [ "$CODESPACE_NAME" != "localhost" ]; then
    BASE_URL="https://${CODESPACE_NAME}-8000.app.github.dev"
else
    BASE_URL="http://localhost:8000"
fi

echo "Testing OctoFit Tracker API"
echo "Base URL: $BASE_URL"
echo "================================"
echo ""

# Test API root endpoint
echo "1. Testing API Root (/):"
curl -s "${BASE_URL}/" | python3 -m json.tool
echo ""
echo "================================"
echo ""

# Test Teams endpoint
echo "2. Testing Teams endpoint (/api/teams/):"
curl -s "${BASE_URL}/api/teams/" | python3 -m json.tool
echo ""
echo "================================"
echo ""

# Test Users endpoint
echo "3. Testing Users endpoint (/api/users/):"
curl -s "${BASE_URL}/api/users/" | python3 -m json.tool
echo ""
echo "================================"
echo ""

# Test Activities endpoint
echo "4. Testing Activities endpoint (/api/activities/):"
curl -s "${BASE_URL}/api/activities/" | python3 -m json.tool
echo ""
echo "================================"
echo ""

# Test Workouts endpoint
echo "5. Testing Workouts endpoint (/api/workouts/):"
curl -s "${BASE_URL}/api/workouts/" | python3 -m json.tool
echo ""
echo "================================"
echo ""

# Test Leaderboard endpoint
echo "6. Testing Leaderboard endpoint (/api/leaderboard/):"
curl -s "${BASE_URL}/api/leaderboard/" | python3 -m json.tool
echo ""
echo "================================"
echo ""

echo "API testing complete!"
