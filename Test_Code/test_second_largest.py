from Code.second_largest import second_largest


def test_second_largest():
    assert second_largest([10, 20, 30, 40, 50]) == 40


def test_unsorted_list():
    assert second_largest([30, 10, 50, 20, 40]) == 40


def test_negative_numbers():
    assert second_largest([-10, -5, -20, -1]) == -5


def test_mixed_positive_negative():
    assert second_largest([-10, 5, 20, -3, 15]) == 15


def test_duplicate_numbers():
    assert second_largest([10, 20, 20, 30, 40]) == 30

    assert second_largest([5, 5, 10, 10, 20]) == 10
