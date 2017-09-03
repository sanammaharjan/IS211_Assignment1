#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Assignment1-Part2-IS211"""

def listDivide(number = [], divide = 2):
    """A function returns the number of integer
    that are divisible by chosen number.
    Args:
        numbers (list): A list if ints
        divide (int, default = 2):divisor
    Returns:
        answer (int): Count of number 0 which mean
        divisble by divide
    Example:
        >>> listDivide([2, 4, 6, 8, 10])
        5
    """
    newNumber = [x % divide for x in number]
    answer = newNumber.count(0)
    return answer

class ListDivideException(Exception):
    """A custom exceptions class."""
    def __init__(self, msg):
        self.msg = msg
    
def testListDivide():
    """Test for listDivide function."""
    
    result = listDivide([1,2,3,4,5])
    if result != 2:
        raise ListDivideException("Failed")
    result = listDivide([2,4,6,8,10])
    if result != 5:
        raise ListDivideException("Failed")
    result = listDivide([30,54,63,98,100], divide=10)
    if result != 2:
        raise ListDivideException("Failed")
    result = listDivide([])
    if result != 0:
        raise ListDivideException("Failed")
    result = listDivide([1,2,3,4,5],1)
    if result != 5:
        raise ListDivideException("Failed")

testListDivide()

