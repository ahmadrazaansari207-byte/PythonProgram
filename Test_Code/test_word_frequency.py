from Code.word_frequency import word_frequency


def test_word_frequency():
    assert word_frequency("hello world hello") == {
        "hello": 2,
        "world": 1
    }


def test_single_word():
    assert word_frequency("hello") == {
        "hello": 1
    }


def test_all_different_words():
    assert word_frequency("apple banana orange") == {
        "apple": 1,
        "banana": 1,
        "orange": 1
    }


def test_empty_sentence():
    assert word_frequency("") == {}


def test_repeated_words():
    assert word_frequency("python python python code code") == {
        "python": 3,
        "code": 2
    }


def test_case_sensitive():
    assert word_frequency("Hello hello HELLO") == {
        "Hello": 1,
        "hello": 1,
        "HELLO": 1
    }
