from Code.reverse_string import reverse_string


def test_reverse_string():
    assert reverse_string("hello") == "olleh"


def test_reverse_string_with_spaces():
    assert reverse_string("yawa og") == "go away"


def test_single_character():
    assert reverse_string("a") == "a"


def test_empty_string():
    assert reverse_string("") == ""


def test_palindrome_string():
    assert reverse_string("madam") == "madam"


def test_uppercase_string():
    assert reverse_string("ELIBOM") == "MOBILE"


def test_numbers_in_string():
    assert reverse_string("12345") == "54321"


def test_mixed_string():
    assert reverse_string("Hello123") == "321olleH"
