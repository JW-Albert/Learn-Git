#! /bin/bash

set -e

clear

source venv/bin/activate

echo "[pytest]
pythonpath = src" > pytest.ini

echo "pytest" > requirements.txt

pip install -r requirements.txt

clear

pytest tests