# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 22:36:17 2017

@author: Sestri4kina

https://www.codewars.com/kata/to-square-root-or-not-to-square-root/train/python
"""

import math

def squareOrNot(num):
    if (math.sqrt(num)).is_integer():
        return math.sqrt(num)
    else:
        return num ** 2

def square_or_square_root(arr):
    return list(map(squareOrNot, arr))

result_1 = square_or_square_root([4, 3, 9, 7, 2, 1 ])
print(result_1 == [2, 9, 3, 49, 4, 1])

result_2 = square_or_square_root([100, 101, 5, 5, 1, 1])
print(result_2 == [10, 10201, 25, 25, 1, 1])