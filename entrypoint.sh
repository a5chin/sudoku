#!/bin/bash

BIND=0.0.0.0:8080
NUM_WORKERS=$(python -c 'import psutil; print(psutil.cpu_count(logical=True) * 2 + 1)')
WORKER_CLASS=uvicorn.workers.UvicornWorker

gunicorn app.main:app --bind ${BIND} \
                      -k ${WORKER_CLASS} \
                      -w ${NUM_WORKERS}

