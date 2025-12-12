# 測試文件說明

## 目錄結構

```
tests/
├── calculator/          # 計算機模組測試
│   └── test_app.py     # Calculator 類別的單元測試
└── docs/               # 文件目錄
    └── README.md       # 本檔案
```

## 測試架構說明

### 測試檔案命名規範

- 測試檔案名稱必須以 `test_` 開頭
- 測試檔案結構需與 `src/` 目錄結構保持一致
- 例如: `src/calculator/app.py` 對應 `tests/calculator/test_app.py`

### 測試函數命名規範

- 測試函數名稱必須以 `test_` 開頭
- 函數名稱應清楚描述測試內容
- 例如: `test_add()`, `test_divide()`, `test_add_with_more()`

## 測試模組說明

### calculator 測試模組

位於 `tests/calculator/test_app.py`，包含以下測試：

#### 基本功能測試

1. **test_add()**: 測試加法運算
   - 驗證基本加法功能

2. **test_subtract()**: 測試減法運算
   - 驗證基本減法功能（包含負數結果）

3. **test_multiply()**: 測試乘法運算
   - 驗證基本乘法功能

4. **test_divide()**: 測試除法運算
   - 驗證正常除法運算
   - 驗證除零異常處理

#### 進階測試

5. **test_add_with_more()**: 參數化測試範例
   - 使用 `pytest.mark.parametrize` 執行多組測試案例
   - 展示如何避免重複程式碼

## Pytest Fixture 說明

### calc fixture

在 `test_app.py` 中定義的 `calc` fixture 提供 Calculator 實例：

- **Scope**: function（預設）
  - 每個測試函數執行前建立新實例
  - 確保測試之間的隔離性

- **使用方式**: 在測試函數參數中注入
  ```python
  def test_add(calc: Calculator) -> None:
      assert calc.add(1, 2) == 3
  ```

## 執行測試

### 執行所有測試

```bash
pytest
```

### 執行特定測試檔案

```bash
pytest tests/calculator/test_app.py
```

### 執行特定測試函數

```bash
pytest tests/calculator/test_app.py::test_add
```

### 顯示詳細輸出

```bash
pytest -v
```

### 顯示 print 輸出

```bash
pytest -s
```

### 顯示測試覆蓋率

```bash
pytest --cov=src tests/
```

## 測試最佳實踐

1. **測試隔離**: 每個測試應該獨立執行，不依賴其他測試的狀態
2. **使用 Fixture**: 透過 fixture 共享測試資源，避免重複程式碼
3. **參數化測試**: 使用 `pytest.mark.parametrize` 測試多組輸入
4. **異常測試**: 使用 `pytest.raises()` 驗證異常是否正確拋出
5. **清晰的斷言**: 使用明確的 assert 語句，便於理解測試意圖

## 相關文件

- 原始碼文件: `../src/docs/README.md`
- 專案根目錄 README: `../../README.md`