from Code.largest_of_three import largest


def test_largest_of_three():
    assert largest(10, 20, 30) == 30 

    assert largest(50, 20, 10) == 50

    assert largest(-25, 30, -30) == 30

    assert largest(-20, 20, 5) == 20

    assert largest(-5, -2, -10) == -2