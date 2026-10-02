from Code.find_duplicates import find_duplicates


def test_find_duplicates():
    assert find_duplicates([1, 2, 3, 2, 4, 3]) == [2, 3]


def test_no_duplicates():
    assert find_duplicates([1, 2, 3, 4, 5]) == []


def test_all_duplicates():
    assert find_duplicates([1, 1, 1, 1]) == [1]


def test_duplicate_at_beginning():
    assert find_duplicates([1, 1, 2, 3, 4]) == [1]


def test_duplicate_at_end():
    assert find_duplicates([1, 2, 3, 4, 4]) == [4]


def test_empty_list():
    assert find_duplicates([]) == []


def test_string_list():
    assert find_duplicates(
        ["apple", "banana", "apple", "orange", "banana"]
    ) == ["apple", "banana"]
