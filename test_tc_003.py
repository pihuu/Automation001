import pytest


def list_add(num_list):
    return sum(num_list)


def list_multipy(num_list):
    mul = 1
    for i in num_list:
        mul *= i
    return mul


number_list = [1, 2, 3, 4]


def test_list_add():
    print('testing addition of list elements')
    assert list_add(number_list) == 10


@pytest.mark.skipif(len(number_list) > 4, reason='here the length of the number list is grater than 4 which is not '
                                                 'allowed')
def test_list_multiply():
    print('testing of list multiplication')
    assert list_multipy(number_list) == 24
