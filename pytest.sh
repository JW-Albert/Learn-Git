#! /bin/bash

source venv/bin/activate

echo "[pytest]
pythonpath = src" > pytest.ini

pytest tests