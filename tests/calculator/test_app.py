from calculator.app import Calculator
import pytest

def test_add() -> None:
    calculator = Calculator()
    assert calculator.add(1, 2) == 3

def test_subtract() -> None:
    calculator = Calculator()
    assert calculator.subtract(1, 2) == -1

def test_multiply() -> None:
    calculator = Calculator()
    assert calculator.multiply(1, 2) == 2

def test_divide() -> None:
    calculator = Calculator()
    assert calculator.divide(1, 2) == 0.5

def test_divide_by_zero() -> None:
    calculator = Calculator()
    with pytest.raises(ZeroDivisionError):
        calculator.divide(1, 0)