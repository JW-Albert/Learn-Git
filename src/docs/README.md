# 原始碼文件說明

## 目錄結構

```
src/
├── calculator/          # 計算機模組
│   ├── __init__.py     # Python 套件初始化檔案
│   └── app.py          # Calculator 類別實作
└── docs/               # 文件目錄
    └── README.md       # 本檔案
```

## 模組說明

### calculator 模組

計算機模組提供基本的數學運算功能。

#### Calculator 類別

位於 `calculator/app.py`，提供以下方法：

- **add(a, b)**: 執行加法運算
  - 參數: 兩個整數
  - 返回: 整數結果

- **subtract(a, b)**: 執行減法運算
  - 參數: 兩個整數（a 為被減數，b 為減數）
  - 返回: 整數結果

- **multiply(a, b)**: 執行乘法運算
  - 參數: 兩個整數
  - 返回: 整數結果

- **divide(a, b)**: 執行除法運算
  - 參數: 兩個整數（a 為被除數，b 為除數）
  - 返回: 浮點數結果
  - 異常: 當除數為 0 時拋出 ZeroDivisionError

## 使用範例

```python
from calculator.app import Calculator

# 建立計算機實例
calc = Calculator()

# 執行運算
result_add = calc.add(10, 20)        # 30
result_subtract = calc.subtract(10, 3)  # 7
result_multiply = calc.multiply(5, 6)   # 30
result_divide = calc.divide(15, 3)      # 5.0

# 處理除零異常
try:
    result = calc.divide(10, 0)
except ZeroDivisionError:
    print("除數不能為零")
```

## 開發規範

1. 所有公開類別和方法都應包含完整的 docstring
2. 使用型別提示（type hints）標註參數和返回值
3. 遵循 PEP 8 程式碼風格規範
4. 確保所有功能都有對應的單元測試

## 相關文件

- 測試文件: `../tests/docs/README.md`
- 專案根目錄 README: `../../README.md`