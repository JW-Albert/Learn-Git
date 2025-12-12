"""
計算機測試模組

此模組包含 Calculator 類別的所有單元測試。
使用 pytest 框架進行測試，包含基本功能測試和參數化測試。

測試涵蓋範圍:
    - 加法運算測試
    - 減法運算測試
    - 乘法運算測試
    - 除法運算測試（包含除零異常測試）
    - 參數化測試範例

執行方式:
    pytest tests/calculator/test_app.py
    或
    pytest tests
"""

from calculator.app import Calculator
from typing import Generator
import pytest


@pytest.fixture
def calc() -> Generator[Calculator, None, None]:
    """
    Calculator 實例的 pytest fixture
    
    此 fixture 會在每個測試函數執行前建立一個新的 Calculator 實例，
    並在測試結束後進行清理。這是 pytest 的預設行為（scope="function"）。
    
    Fixture Scope 說明:
        - function (預設): 每個測試函數建立一次，最常用於確保測試隔離
        - class: 每個測試類別建立一次
        - module: 每個測試模組建立一次
        - session: 整個測試流程只建立一次，用於共享資源
    
    參數:
        無
    
    產生:
        Calculator: Calculator 類別的實例
    
    範例:
        測試函數可以透過參數注入使用此 fixture:
        def test_add(calc: Calculator) -> None:
            result = calc.add(1, 2)
            assert result == 3
    """
    # 建立 Calculator 實例
    calculator = Calculator()
    # 使用 yield 將控制權交給測試函數
    yield calculator
    # 測試結束後的清理工作（此範例中不需要，但保留以展示模式）


def test_add(calc: Calculator) -> None:
    """
    測試加法運算功能
    
    驗證 Calculator.add() 方法能正確執行加法運算。
    
    參數:
        calc (Calculator): 透過 pytest fixture 注入的 Calculator 實例
    
    測試案例:
        - 驗證 1 + 2 = 3
    """
    assert calc.add(1, 2) == 3


def test_subtract(calc: Calculator) -> None:
    """
    測試減法運算功能
    
    驗證 Calculator.subtract() 方法能正確執行減法運算。
    
    參數:
        calc (Calculator): 透過 pytest fixture 注入的 Calculator 實例
    
    測試案例:
        - 驗證 1 - 2 = -1（負數結果）
    """
    assert calc.subtract(1, 2) == -1


def test_multiply(calc: Calculator) -> None:
    """
    測試乘法運算功能
    
    驗證 Calculator.multiply() 方法能正確執行乘法運算。
    
    參數:
        calc (Calculator): 透過 pytest fixture 注入的 Calculator 實例
    
    測試案例:
        - 驗證 1 * 2 = 2
    """
    assert calc.multiply(1, 2) == 2


def test_divide(calc: Calculator) -> None:
    """
    測試除法運算功能
    
    驗證 Calculator.divide() 方法能正確執行除法運算，
    並確保在除數為零時能正確拋出 ZeroDivisionError 異常。
    
    參數:
        calc (Calculator): 透過 pytest fixture 注入的 Calculator 實例
    
    測試案例:
        - 驗證 1 / 2 = 0.5（正常除法）
        - 驗證 1 / 0 會拋出 ZeroDivisionError（除零異常）
    
    注意:
        使用 pytest.raises() 來驗證異常是否正確拋出
    """
    # 測試正常除法運算
    assert calc.divide(1, 2) == 0.5
    
    # 測試除零異常
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)


@pytest.mark.parametrize("n1, n2, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (3, 4, 7),
])
def test_add_with_more(calc: Calculator, n1: int, n2: int, expected: int) -> None:
    """
    使用參數化測試驗證加法運算
    
    此測試使用 pytest.mark.parametrize 裝飾器來執行多組測試案例，
    避免重複撰寫相似的測試程式碼。pytest 會為每個參數組合執行一次測試。
    
    參數:
        calc (Calculator): 透過 pytest fixture 注入的 Calculator 實例
        n1 (int): 第一個運算元
        n2 (int): 第二個運算元
        expected (int): 預期的運算結果
    
    測試案例:
        - (1, 2) -> 3
        - (2, 3) -> 5
        - (3, 4) -> 7
    
    注意:
        pytest.mark.parametrize 會自動為每個參數組合建立獨立的測試案例，
        在測試報告中會顯示為多個測試項目。
    """
    assert calc.add(n1, n2) == expected 