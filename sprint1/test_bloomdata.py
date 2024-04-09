"""
This module tests
bloodata function of they are running well
"""
import pytest

import sprint1.bloomdata as sblm

#the function name has to start with test
def test_increment_int():
    """
    The function checks if the increment 
    function parameter is given a 3 gives a 4
    """
    #assert statement is important
    assert sblm.increment(3) == 4
    assert sblm.increment(-2) == -1

def test_increament_float():
    """
    The function checks if the increment 
    function parameter is given a 1.5 gives a 2.5
    """
    assert sblm.increment(1.5) == 2.5

# check the data type passed
def test_increment_int_return_type():
    """
    The function checks if the 
    the return statement is an integer
    """
    assert isinstance(sblm.increment(3), int)

def test_decrease_int():
    """
    The function checks if the decrease 
    function parameter is given a 3 gives a 2
    """
    assert sblm.decrease(3) == 2

def test_count_a():
    """
    The function checks if the
    length is 4
    """
    assert sblm.cout([1,2,3,4]) == 4


def test_sum():
    """
    The function checks if the sum 
    function is 15
    """
    assert sblm.add_up([4,5,6]) == 15
