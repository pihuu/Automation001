import pytest


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def test_add():
    assert add(2, 3) == 5
    assert add(5, 7) == 12


@pytest.mark.skip('message:there is an error dev team will fix in next release')
def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(8, 3) == 5
