#!/bin/bash

alembic upgrade head
cd src

# Check if RELOAD_APP is set to "true"
if [ "$RELOAD_APP" = "true" ]; then
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
else
    uvicorn main:app --host 0.0.0.0 --port 8000
fi
