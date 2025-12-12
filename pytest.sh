#! /bin/bash

set -e

# 安全地執行 clear 命令（在 CI/CD 環境中會自動跳過）
safe_clear() {
    if [ -t 1 ] && [ -n "$TERM" ] && command -v clear >/dev/null 2>&1; then
        clear 2>/dev/null || true
    fi
}

# 執行清屏（在 CI/CD 環境中會自動跳過）
safe_clear

source venv/bin/activate

echo "[pytest]
pythonpath = src" > pytest.ini

# 執行清屏（在 CI/CD 環境中會自動跳過）
safe_clear

pytest tests

deactivate

rm pytest.ini