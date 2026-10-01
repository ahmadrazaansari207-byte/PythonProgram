from Code.reverse_number import reverse_number


def test_reverse_number():
    assert reverse_number(12345) == 54321


def test_reverse_number_single_digit():
    assert reverse_number(7) == 7


def test_reverse_number_with_zero():
    assert reverse_number(120) == 21


def test_reverse_number_palindrome():
    assert reverse_number(121) == 121
    
    assert reverse_number(123321) == 123321