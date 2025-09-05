#!/bin/bash

source ./set_env.sh

# Run the docker-compose command
docker-compose build --no-cache
docker-compose up -d