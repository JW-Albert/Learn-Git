#! /bin/bash

set -e

# 只在 TERM 環境變數存在時執行 clear（避免在 CI/CD 環境中出錯）
[ -n "$TERM" ] && clear

source venv/bin/activate

echo "[pytest]
pythonpath = src" > pytest.ini

echo "pytest" > requirements.txt

pip install -r requirements.txt

# 只在 TERM 環境變數存在時執行 clear（避免在 CI/CD 環境中出錯）
[ -n "$TERM" ] && clear

pytest tests