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

# 檢查是否在 CI/CD 環境中（GitHub Actions 通常已經有 Python）
# 在 CI/CD 環境中跳過系統套件安裝，因為 Python 已經預裝
if [ -z "$CI" ] && [ -z "$GITHUB_ACTIONS" ]; then
    # 只在非 CI/CD 環境中更新和安裝套件
    # 使用 || true 避免在沒有 sudo 權限時失敗
    if command -v sudo >/dev/null 2>&1; then
        sudo apt update && sudo apt upgrade -y || true
        sudo apt install python3 python3-pip python3-venv -y || true
    fi
fi

# 建立虛擬環境（如果不存在）
if [ ! -d "venv" ]; then
    # 嘗試使用 python3，如果不存在則使用 python
    if command -v python3 >/dev/null 2>&1; then
        python3 -m venv venv
    elif command -v python >/dev/null 2>&1; then
        python -m venv venv
    else
        echo "錯誤: 找不到 Python 命令"
        exit 1
    fi
fi

source venv/bin/activate

# 升級 pip（建議做法）
pip install --upgrade pip || true

# 安裝依賴（如果 requirements.txt 存在）
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

deactivate

# 執行清屏（在 CI/CD 環境中會自動跳過）
safe_clear

echo "Done"