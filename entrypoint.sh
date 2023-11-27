#!/bin/bash
APP_PORT=${PORT:-8000}
cd /app/src
/opt/venv/bin/uvicorn main:app --host "0.0.0.0" --port "${APP_PORT}"