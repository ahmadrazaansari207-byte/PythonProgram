from Code.missing_number import missing_number


def test_missing_number():
    assert missing_number([1, 2, 3, 5]) == 4


def test_missing_first_number():
    assert missing_number([2, 3, 4, 5]) == 1


def test_missing_last_number():
    assert missing_number([1, 2, 3, 4]) == 5


def test_missing_middle_number():
    assert missing_number([1, 2, 3, 4, 6, 7]) == 5


def test_two_numbers():
    assert missing_number([1, 2]) == 3


def test_unsorted_list():
    assert missing_number([3, 1, 5, 2]) == 4
