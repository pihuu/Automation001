import pytest


def add(num1, num2):
    return num1 + num2


print('addition result')


@pytest.mark.Smoke
@pytest.mark.Regression
def test_add():
    print('inside test case of addition')
    assert add(2, 3) == 5


def mult(number1, number2):
    return number1 * number2


@pytest.mark.Sanity

def test_mult():
    print('inside test case of multiplication')
    assert mult(2, 4) == 8
