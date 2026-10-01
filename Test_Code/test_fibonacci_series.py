from Code.fibonacci_series import fibonacci_series

def test_fibonacci():
    assert fibonacci_series(5) == "0 1 1 2 3 "

    assert fibonacci_series(7) == "0 1 1 2 3 5 8 "

    assert fibonacci_series(1) == "0 "


def test_zero():
    assert fibonacci_series(0) == "Enter a positive number"

def test_negative():
    assert fibonacci_series(-5) == "Enter a positive number"