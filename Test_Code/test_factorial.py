from Code.factorial import factorial

def test_positive_factorial():
    assert factorial(5) == 120
    assert factorial(6) == 720


def test_one_factorial():
    assert factorial(1) == 1


def test_zero_factorial():
    assert factorial(0) == 1


def test_negative_factorial():
    assert factorial(-5) == "Factorial is not defined for negative numbers"