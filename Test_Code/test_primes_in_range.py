from Code.primes_in_range import primes_in_range


def test_prime_numbers_in_range():
    assert primes_in_range(1, 10) == [2, 3, 5, 7]

    assert primes_in_range(1, 20) == [2, 3, 5, 7, 11, 13, 17, 19]

    assert primes_in_range(10, 20) == [11, 13, 17, 19]


def test_single_prime_number():
    assert primes_in_range(7, 7) == [7]


def test_no_prime_numbers():
    assert primes_in_range(8, 10) == []


def test_range_includes_zero():
    assert primes_in_range(0, 10) == [2, 3, 5, 7]
