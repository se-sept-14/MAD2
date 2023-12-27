#!/bin/bash

# Stop any running containers
echo "Stopping running containers ..."
docker compose down -v

# Start docker compose service
echo "Starting up the containers ..."
docker compose up --build -d
