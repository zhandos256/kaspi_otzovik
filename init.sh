#!/bin/sh

# create virtualenv
/usr/bin/python3 -m venv .env
. ./.env/bin/activate

pip install -U pip && pip install -r requirements.txt

# create folders
mkdir ./src/migrations/versions
mkdir ./src/locales

cd ./src

# init db
python init_db.py

# create inital migrations
alembic revision -m "initial"
alembic upgrade head
