# Learn-Git: GitHub Actions 與 pytest 學習專案

版本: **v1.0.0**

這是一個用於學習 **GitHub Actions** 和 **pytest** 的教學專案。透過實作一個簡單的計算機模組，學習如何設置 CI/CD 自動化流程、撰寫單元測試，以及使用 GitHub Actions 進行持續整合與部署。

## 學習目標

本專案旨在幫助學習者掌握以下技能：

- **pytest 測試框架**：學習如何撰寫和執行單元測試
- **GitHub Actions**：學習如何設置 CI/CD 自動化工作流程
- **Python 專案結構**：了解標準的 Python 專案組織方式
- **測試最佳實踐**：學習測試 fixture、參數化測試等進階技巧
- **CI/CD 流程**：學習自動化測試與部署流程

## 專案特色

### 學習內容

- **pytest 測試框架**
  - 基本測試函數撰寫
  - 使用 fixture 共享測試資源
  - 參數化測試（parametrize）
  - 異常測試（pytest.raises）
  - 測試組織與結構

- **GitHub Actions CI/CD**
  - 工作流程配置（workflow）
  - 自動化測試觸發
  - 環境變數與 secrets 管理
  - 自動化部署流程
  - 多環境配置

### 技術實作

- 基本四則運算：加法、減法、乘法、除法
- 完整的型別提示（Type Hints）
- 除零異常處理
- 完整的單元測試覆蓋
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

## pytest 學習重點

本專案展示了如何使用 pytest 進行單元測試。以下是學習重點：

### pytest 基本概念

- **測試發現**: pytest 自動發現以 `test_` 開頭的檔案和函數
- **斷言**: 使用 Python 的 `assert` 語句進行測試
- **Fixture**: 用於設置和清理測試資源
- **參數化測試**: 使用 `@pytest.mark.parametrize` 執行多組測試案例
- **異常測試**: 使用 `pytest.raises()` 驗證異常

### 執行測試

#### 使用測試腳本

```bash
chmod +x pytest.sh
./pytest.sh
```

#### 直接使用 pytest

```bash
# 執行所有測試
pytest tests

# 執行特定測試檔案
pytest tests/calculator/test_app.py

# 執行特定測試函數
pytest tests/calculator/test_app.py::test_add

# 顯示詳細輸出
pytest -v

# 顯示測試覆蓋率（需要安裝 pytest-cov）
pytest --cov=src tests/
```

### 測試範例學習

本專案包含以下測試範例，可作為學習參考：

1. **基本功能測試** (`test_add`, `test_subtract`, `test_multiply`)
   - 學習如何撰寫簡單的測試函數
   - 學習如何使用 fixture 注入測試資源

2. **異常測試** (`test_divide`)
   - 學習如何使用 `pytest.raises()` 測試異常
   - 學習如何測試多個測試案例

3. **參數化測試** (`test_add_with_more`)
   - 學習如何使用 `@pytest.mark.parametrize` 裝飾器
   - 學習如何避免重複的測試程式碼

4. **Fixture 使用** (`calc` fixture)
   - 學習如何定義和使用 fixture
   - 學習 fixture 的 scope 概念（function, class, module, session）

### 測試涵蓋範圍

- 加法運算測試
- 減法運算測試
- 乘法運算測試
- 除法運算測試（包含除零異常測試）
- 參數化測試範例

## GitHub Actions 學習重點

本專案展示了如何使用 GitHub Actions 進行 CI/CD 自動化。以下是學習重點：

### 測試工作流程 (`.github/workflows/test.yaml`)

學習如何設置自動化測試流程：

- **觸發條件**: 推送到 `main` 分支或開啟 Pull Request
- **執行內容**: 自動執行所有單元測試
- **學習要點**:
  - 如何使用 `actions/checkout` 檢查程式碼
  - 如何使用 `actions/setup-python` 設置 Python 環境
  - 如何執行自訂腳本（`env.sh`, `pytest.sh`）
  - 如何處理環境變數（如 `TERM`）

### 部署工作流程 (`.github/workflows/deploy.yaml`)

學習如何設置自動化部署流程：

- **觸發條件**: 推送到 `main` 分支或建立版本標籤（`v*`）
- **執行內容**: 自動部署到遠端伺服器
- **學習要點**:
  - 如何使用 `appleboy/scp-action` 進行檔案傳輸
  - 如何使用 GitHub Secrets 管理敏感資訊
  - 如何使用 GitHub Variables 管理配置變數
  - 如何設置部署觸發條件

### GitHub Actions 關鍵概念

- **Workflow**: 自動化流程定義
- **Job**: 工作流程中的任務
- **Step**: 任務中的執行步驟
- **Action**: 可重用的工作單元
- **Secrets**: 安全儲存敏感資訊
- **Variables**: 儲存配置變數

## 學習路徑建議

### 初學者

1. 先了解專案結構和計算機模組的基本功能
2. 閱讀測試檔案，理解 pytest 的基本用法
3. 嘗試執行測試，觀察測試結果
4. 查看 GitHub Actions 工作流程配置

### 進階學習

1. 研究 fixture 的使用方式和 scope 概念
2. 學習參數化測試的進階用法
3. 深入了解 GitHub Actions 的各種觸發條件
4. 學習如何設置 secrets 和 variables
5. 嘗試修改工作流程，添加新的步驟

### 實作練習

1. 為計算機添加新功能（如次方運算）
2. 為新功能撰寫對應的測試
3. 修改 GitHub Actions 工作流程
4. 嘗試設置不同的觸發條件

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

## 學習資源

### pytest 相關

- [pytest 官方文件](https://docs.pytest.org/)
- [pytest 最佳實踐](https://docs.pytest.org/en/stable/goodpractices.html)
- [pytest fixture 說明](https://docs.pytest.org/en/stable/fixture.html)

### GitHub Actions 相關

- [GitHub Actions 官方文件](https://docs.github.com/en/actions)
- [GitHub Actions 工作流程語法](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [GitHub Actions 市場](https://github.com/marketplace?type=actions)

## 版本歷史

### v1.0.0 (當前版本)

- 初始版本發布
- 實現基本四則運算功能作為學習範例
- 完整的 pytest 單元測試範例
- GitHub Actions CI/CD 工作流程範例
- 完整的中文文件與註解
- 詳細的學習說明文件

## 授權

本專案僅供學習使用。

## 貢獻

歡迎提交 Issue 或 Pull Request 來改進此學習專案。如果您有更好的學習範例或教學內容，歡迎分享！

## 聯絡資訊

如有任何問題或建議，請透過 GitHub Issues 聯繫。

---

**注意**: 本專案為**學習用途**，主要目的是幫助學習者理解 GitHub Actions 和 pytest 的使用方式。計算機功能僅作為學習範例，實際生產環境使用請自行評估安全性與穩定性。