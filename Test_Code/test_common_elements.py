from Code.common_elements import common_elements


def test_common_elements():
    assert common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]


def test_no_common_elements():
    assert common_elements([1, 2, 3], [4, 5, 6]) == []


def test_all_common_elements():
    assert common_elements([1, 2, 3], [1, 2, 3]) == [1, 2, 3]


def test_empty_first_list():
    assert common_elements([], [1, 2, 3]) == []


def test_empty_second_list():
    assert common_elements([1, 2, 3], []) == []


def test_string_lists():
    assert common_elements(
        ["apple", "banana", "orange"],
        ["banana", "orange", "grape"]
    ) == ["banana", "orange"]
