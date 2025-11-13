#!/bin/bash

source /opt/venv/bin/activate

# Navigate to code directory
cd /code

# Set the port (use PORT env var, default to 8000)
RUN_PORT=${PORT:-8000}
RUN_HOST=${HOST:-0.0.0.0}

echo "Starting server on port $RUN_PORT"

# Start the FastAPI application
gunicorn -k uvicorn.workers.UvicornWorker -b $RUN_HOST:$RUN_PORT main:app