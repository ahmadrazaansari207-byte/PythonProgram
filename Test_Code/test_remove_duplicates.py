from Code.remove_duplicates import remove_duplicates


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]


def test_no_duplicates():
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_all_duplicates():
    assert remove_duplicates([1, 1, 1, 1]) == [1]


def test_empty_list():
    assert remove_duplicates([]) == []


def test_string_list():
    assert remove_duplicates(["apple", "banana", "apple", "orange"]) == [
        "apple", "banana", "orange"
    ]
