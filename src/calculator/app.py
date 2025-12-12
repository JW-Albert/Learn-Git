"""
計算機模組

此模組提供基本的數學運算功能，包括加法、減法、乘法和除法。
所有運算方法都支援整數輸入，除法運算會返回浮點數結果。

範例:
    >>> calc = Calculator()
    >>> calc.add(1, 2)
    3
    >>> calc.divide(10, 2)
    5.0
"""


class Calculator:
    """
    計算機類別
    
    提供基本的四則運算功能。所有方法都包含完整的型別提示，
    並在除法運算時檢查除數是否為零。
    
    屬性:
        無公開屬性
    
    方法:
        add: 執行加法運算
        subtract: 執行減法運算
        multiply: 執行乘法運算
        divide: 執行除法運算（會檢查除數是否為零）
    
    範例:
        >>> calculator = Calculator()
        >>> calculator.add(5, 3)
        8
        >>> calculator.multiply(4, 7)
        28
        >>> calculator.divide(15, 3)
        5.0
    """
    
    def add(self, a: int, b: int) -> int:
        """
        執行加法運算
        
        將兩個整數相加並返回結果。
        
        參數:
            a (int): 第一個運算元
            b (int): 第二個運算元
        
        返回:
            int: 兩個數字的總和
        
        範例:
            >>> calc = Calculator()
            >>> calc.add(10, 20)
            30
            >>> calc.add(-5, 5)
            0
        """
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """
        執行減法運算
        
        從第一個數字減去第二個數字並返回結果。
        
        參數:
            a (int): 被減數
            b (int): 減數
        
        返回:
            int: 兩個數字的差
        
        範例:
            >>> calc = Calculator()
            >>> calc.subtract(10, 3)
            7
            >>> calc.subtract(5, 8)
            -3
        """
        return a - b

    def multiply(self, a: int, b: int) -> int:
        """
        執行乘法運算
        
        將兩個整數相乘並返回結果。
        
        參數:
            a (int): 第一個運算元
            b (int): 第二個運算元
        
        返回:
            int: 兩個數字的乘積
        
        範例:
            >>> calc = Calculator()
            >>> calc.multiply(6, 7)
            42
            >>> calc.multiply(-3, 4)
            -12
        """
        return a * b

    def divide(self, a: int, b: int) -> float:
        """
        執行除法運算
        
        將第一個數字除以第二個數字並返回浮點數結果。
        如果除數為零，會拋出 ZeroDivisionError 異常。
        
        參數:
            a (int): 被除數
            b (int): 除數（不能為零）
        
        返回:
            float: 兩個數字相除的結果
        
        異常:
            ZeroDivisionError: 當除數 b 為 0 時拋出
        
        範例:
            >>> calc = Calculator()
            >>> calc.divide(10, 2)
            5.0
            >>> calc.divide(7, 2)
            3.5
            >>> calc.divide(5, 0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError
        """
        if b == 0:
            raise ZeroDivisionError("除數不能為零")

        return a / b