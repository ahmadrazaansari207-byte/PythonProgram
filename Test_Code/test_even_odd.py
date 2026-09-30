from Code.even_odd import even_odd


def test_even_number():
    assert even_odd(10) == "The given no. 10 is even"


def test_odd_number():
    assert even_odd(7) == "The given no. 7 is odd"

def test_zero():
    assert even_odd(0) == "The given no. 0 is even"


def test_negative_even():
    assert even_odd(-4) == "The given no. -4 is even"


def test_negative_odd():
    assert even_odd(-7) == "The given no. -7 is odd"