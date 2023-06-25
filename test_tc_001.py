import pytest


@pytest.fixture(scope="module")
def fixture_code():
    print("\nfixture code will execute before test cases")
    print("-------------------------")
    yield
    print("\nfixture code will execute after test cases")
    print("-------------------------")


def add(num1, num2):
    return num1 + num2


print('addition result')


def test_add(fixture_code):
    print('inside test case of addition')
    assert add(2, 3) == 5, "the output is wrong as it is not matching with expected"


def mult(number1, number2):
    return number1 * number2


def test_mult(fixture_code):
    print('inside test case of multiplication')
    assert mult(2, 4) == 8
