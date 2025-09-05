#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e
source ./set_env.sh

VENV_DIR=".venv"
REQUIREMENTS=false

if [[ "$1" == "-r" ]]; then
    REQUIREMENTS=true
fi

# Create a virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
  REQUIREMENTS=true
  echo "--- Virtual environment not found. Creating one. (using python3.9) ---"
  python3.9 -m venv $VENV_DIR
fi

# Activate the virtual environment based on the operating system
if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
  # Linux or macOS (darwin)
  source $VENV_DIR/bin/activate
elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" ]]; then
  # Windows running Git Bash or similar
  source $VENV_DIR/Scripts/activate
fi


if [ "$REQUIREMENTS" = true ] ; then
  echo "--- Installing dependencies from requirements.txt ---"
  pip install --no-cache-dir -r requirements.txt
fi

export PORT=8000
cd app
echo "--- Starting application ---"
#python app.py
uvicorn app:app --host 0.0.0.0 --port $PORT