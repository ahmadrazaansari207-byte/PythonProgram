from Code.char_frequency import char_frequency


def test_character_frequency():
    assert char_frequency("hello") == {
        "h": 1,
        "e": 1,
        "l": 2,
        "o": 1
    }


def test_repeated_characters():
    assert char_frequency("aaa") == {
        "a": 3
    }


def test_all_different_characters():
    assert char_frequency("abc") == {
        "a": 1,
        "b": 1,
        "c": 1
    }


def test_empty_string():
    assert char_frequency("") == {}


def test_with_spaces():
    assert char_frequency("hello world") == {
        "h": 1,
        "e": 1,
        "l": 3,
        "o": 2,
        "w": 1,
        "r": 1,
        "d": 1
    }


def test_uppercase_and_lowercase():
    assert char_frequency("AaA") == {
        "A": 2,
        "a": 1
    }


def test_numbers():
    assert char_frequency("1122") == {
        "1": 2,
        "2": 2
    }
