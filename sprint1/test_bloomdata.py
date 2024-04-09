import pytest
import sprint1.bloomdata as sblm

#the function name has to start with test
def test_increment_int():
    #assert statement is important
    assert sblm.increment(3) == 4
    assert sblm.increment(-2) == -1

def test_increament_float():
    assert sblm.increment(1.5) == 2.5


# check the data type passed
def test_increment_int_return_type():
    assert isinstance(sblm.increment(3), int)

def test_decrease_int():
    assert sblm.decrease(3) == 2

def test_count_a():
    assert sblm.cout([1,2,3,4]) == 4


def test_sum():
    assert sblm.ar([4,5,6]) == 15
