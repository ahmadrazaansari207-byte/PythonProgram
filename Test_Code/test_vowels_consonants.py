from Code.vowels_consonants import vowels_consonants


def test_vowels_and_consonants():
    assert vowels_consonants("Hello") == (2, 3)


def test_all_vowels():
    assert vowels_consonants("aeiou") == (5, 0)


def test_all_consonants():
    assert vowels_consonants("bcdfg") == (0, 5)


def test_uppercase_letters():
    assert vowels_consonants("HELLO") == (2, 3)


def test_mixed_case():
    assert vowels_consonants("Python") == (1, 5)


def test_with_spaces():
    assert vowels_consonants("Hello World") == (3, 7)


def test_empty_string():
    assert vowels_consonants("") == (0, 0)


def test_with_numbers():
    assert vowels_consonants("Hello123") == (2, 3)
