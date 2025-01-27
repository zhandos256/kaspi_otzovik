#!/bin/bash

cd src

if ls migrations/versions/*.py 1>/dev/null 2>&1; then
    echo "Миграции уже существуют, пропускаем создание новой."
else
    alembic revision --autogenerate -m "initial"
    alembic upgrade head
fi