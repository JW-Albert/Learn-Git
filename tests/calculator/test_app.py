from calculator.app import Calculator

def test_add() -> None:
    calculator = Calculator()
    assert calculator.add(1, 2) == 3

def test_subtract() -> None:
    calculator = Calculator()
    assert calculator.subtract(1, 2) == -1

def test_multiply() -> None:
    calculator = Calculator()
    assert calculator.multiply(1, 2) == 2