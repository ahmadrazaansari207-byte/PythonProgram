from Code.prime_number import prime_number


def test_prime_number():
    assert prime_number(2) == "The given no. is Prime"

    assert prime_number(5) == "The given no. is Prime"


def test_non_prime_number():
    assert prime_number(4) == "The given no. is not Prime"

    assert prime_number(10) == "The given no. is not Prime"


def test_zero():
    assert prime_number(0) == "The given no. is not Prime"


def test_one():
    assert prime_number(1) == "The given no. is not Prime"


def test_negative_number():
    assert prime_number(-7) == "The given no. is not Prime"
