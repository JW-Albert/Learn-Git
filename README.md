# Calculator 計算機專案

版本: **v1.0.0**

一個使用 Python 開發的簡單計算機模組，提供基本的四則運算功能。專案包含完整的單元測試、CI/CD 自動化流程和詳細的文件說明。

## 功能特色

- 基本四則運算：加法、減法、乘法、除法
- 完整的型別提示（Type Hints）
- 除零異常處理
- 完整的單元測試覆蓋
- GitHub Actions CI/CD 自動化
- 詳細的中文文件與註解

## 專案結構

```
Learn-Git/
├── src/                    # 原始碼目錄
│   ├── calculator/         # 計算機模組
│   │   ├── __init__.py     # 套件初始化檔案
│   │   └── app.py          # Calculator 類別實作
│   └── docs/               # 原始碼文件
│       └── README.md       # 原始碼說明文件
├── tests/                  # 測試目錄
│   ├── calculator/         # 計算機測試模組
│   │   └── test_app.py     # Calculator 單元測試
│   └── docs/               # 測試文件
│       └── README.md       # 測試說明文件
├── .github/                # GitHub 配置
│   └── workflows/          # GitHub Actions 工作流程
│       ├── test.yaml       # 測試工作流程
│       └── deploy.yaml     # 部署工作流程
├── env.sh                  # 環境設置腳本
├── pytest.sh               # 測試執行腳本
├── deploy.sh               # 部署腳本
└── README.md               # 本檔案
```

## 安裝說明

### 前置需求

- Python 3.7 或更高版本
- pip（Python 套件管理器）

### 安裝步驟

1. 複製專案到本地：

```bash
git clone <repository-url>
cd Learn-Git
```

2. 執行環境設置腳本：

```bash
chmod +x env.sh
./env.sh
```

此腳本會自動：
- 安裝 Python 和相關套件（僅在非 CI/CD 環境）
- 建立虛擬環境（venv）
- 安裝專案依賴（pytest）

### 手動安裝

如果您想手動設置環境：

```bash
# 建立虛擬環境
python3 -m venv venv

# 啟動虛擬環境
source venv/bin/activate  # Linux/macOS
# 或
venv\Scripts\activate      # Windows

# 安裝依賴
pip install pytest
```

## 使用範例

### 基本使用

```python
from calculator.app import Calculator

# 建立計算機實例
calc = Calculator()

# 執行加法運算
result = calc.add(10, 20)
print(result)  # 輸出: 30

# 執行減法運算
result = calc.subtract(10, 3)
print(result)  # 輸出: 7

# 執行乘法運算
result = calc.multiply(5, 6)
print(result)  # 輸出: 30

# 執行除法運算
result = calc.divide(15, 3)
print(result)  # 輸出: 5.0
```

### 異常處理

```python
from calculator.app import Calculator

calc = Calculator()

# 處理除零異常
try:
    result = calc.divide(10, 0)
except ZeroDivisionError as e:
    print(f"錯誤: {e}")  # 輸出: 錯誤: 除數不能為零
```

## API 文件

### Calculator 類別

#### 方法

##### `add(a: int, b: int) -> int`

執行加法運算。

- **參數**:
  - `a` (int): 第一個運算元
  - `b` (int): 第二個運算元
- **返回**: `int` - 兩個數字的總和

##### `subtract(a: int, b: int) -> int`

執行減法運算。

- **參數**:
  - `a` (int): 被減數
  - `b` (int): 減數
- **返回**: `int` - 兩個數字的差

##### `multiply(a: int, b: int) -> int`

執行乘法運算。

- **參數**:
  - `a` (int): 第一個運算元
  - `b` (int): 第二個運算元
- **返回**: `int` - 兩個數字的乘積

##### `divide(a: int, b: int) -> float`

執行除法運算。

- **參數**:
  - `a` (int): 被除數
  - `b` (int): 除數（不能為零）
- **返回**: `float` - 兩個數字相除的結果
- **異常**: 當除數 `b` 為 0 時拋出 `ZeroDivisionError`

## 測試

### 執行測試

使用提供的測試腳本：

```bash
chmod +x pytest.sh
./pytest.sh
```

或直接使用 pytest：

```bash
# 執行所有測試
pytest tests

# 執行特定測試檔案
pytest tests/calculator/test_app.py

# 執行特定測試函數
pytest tests/calculator/test_app.py::test_add

# 顯示詳細輸出
pytest -v

# 顯示測試覆蓋率
pytest --cov=src tests/
```

### 測試涵蓋範圍

- 加法運算測試
- 減法運算測試
- 乘法運算測試
- 除法運算測試（包含除零異常測試）
- 參數化測試範例

## CI/CD

專案使用 GitHub Actions 進行持續整合和部署：

### 測試工作流程

- **觸發條件**: 推送到 `main` 分支或開啟 Pull Request
- **執行內容**: 自動執行所有單元測試
- **配置檔案**: `.github/workflows/test.yaml`

### 部署工作流程

- **觸發條件**: 推送到 `main` 分支或建立版本標籤（`v*`）
- **執行內容**: 自動部署到遠端伺服器
- **配置檔案**: `.github/workflows/deploy.yaml`

## 開發指南

### 程式碼風格

- 遵循 PEP 8 Python 程式碼風格規範
- 使用型別提示（Type Hints）
- 所有公開類別和方法都包含完整的 docstring
- 使用繁體中文撰寫註解和文件

### 提交規範

- 使用清晰的提交訊息
- 確保所有測試通過後再提交
- 遵循專案的 Git 工作流程

## 相關文件

- [原始碼文件](src/docs/README.md)
- [測試文件](tests/docs/README.md)

## 版本歷史

### v1.0.0 (當前版本)

- 初始版本發布
- 實現基本四則運算功能
- 完整的單元測試覆蓋
- GitHub Actions CI/CD 整合
- 完整的中文文件與註解

## 授權

本專案僅供學習使用。

## 貢獻

歡迎提交 Issue 或 Pull Request 來改進此專案。

## 聯絡資訊

如有任何問題或建議，請透過 GitHub Issues 聯繫。

---

**注意**: 本專案為學習用途，實際生產環境使用請自行評估安全性與穩定性。