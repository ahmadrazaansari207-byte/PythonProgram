from Code.sum_of_digits import sum_of_digits


def test_sum_of_digits():
    assert sum_of_digits(12345) == 15

    assert sum_of_digits(9889) == 34


def test_sum_of_digits_single_digit():
    assert sum_of_digits(7) == 7


def test_sum_of_digits_zero():
    assert sum_of_digits(0) == 0


def test_sum_of_digits_repeated_digits():
    assert sum_of_digits(1111) == 4


def test_sum_of_digits_with_zero():
    assert sum_of_digits(10203) == 6
