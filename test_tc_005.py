import pytest


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


@pytest.mark.Smoke
@pytest.mark.Regression
def test_add():
    print('testing add result')
    assert add(2, 3) == 5
    assert add(5, 7) == 12


@pytest.mark.Sanity
def test_subtract():
    print('testing subtraction result')
    assert subtract(10, 5) == 5
    assert subtract(8, 3) == 5
