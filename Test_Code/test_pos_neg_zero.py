from Code.pos_neg_zero import pos_neg_zero


def test_positive_number():
    assert pos_neg_zero(10) == "The given no. is Positive"


def test_negative_number():
    assert pos_neg_zero(-7) == "The given no. is Negative"


def test_zero():
    assert pos_neg_zero(0) == "The given no. is Zero"


def test_positive_one():
    assert pos_neg_zero(1) == "The given no. is Positive"


def test_negative_one():
    assert pos_neg_zero(-1) == "The given no. is Negative"