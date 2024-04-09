"""
This module demonstrates:
increament a a number by 1
decrease a a number by 1
count the elements in an array
Sums up all the elements in an array

They are within a function
"""



def increment(num):
    """
    The above function 
    increament a a number by 1 
    """
    return num  + 1

def decrease(num):
    """
    The above function 
    decreases a a number by 1 
    """
    return num - 1


def cout(array_1):
    """
    The above function 
    counts the of elements in array
    """
    return len(array_1)

def add_up(array_2):
    """
    The above function 
    counts the of elements in array
    """
    sum_up = 0
    for ele_arr in array_2:
        sum_up +=ele_arr
    return sum
