#!/bin/bash

alembic upgrade head

uvicorn src.main:app --host '::' --port 8000

