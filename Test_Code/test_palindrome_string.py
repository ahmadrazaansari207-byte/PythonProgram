from Code.palindrome_string import palindrome_string


def test_palindrome_string():
    assert palindrome_string("madam") == True


def test_non_palindrome_string():
    assert palindrome_string("hello") == False


def test_single_character():
    assert palindrome_string("a") == True


def test_empty_string():
    assert palindrome_string("") == True


def test_uppercase_string():
    assert palindrome_string("MADAM") == True


def test_string_with_numbers():
    assert palindrome_string("12321") == True
