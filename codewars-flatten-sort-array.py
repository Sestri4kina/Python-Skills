# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 11:40:50 2017

@author: Sestri4kina

https://www.codewars.com/kata/flatten-and-sort-an-array/train/python
"""
def flatten_and_sort(array):
    if len(array) == 0:
        return array
    new_arr = []
    for el in array:
        new_arr.extend(el)
    return sorted(new_arr)

res_1 = flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]])
print(res_1 == [1, 2, 3, 4, 5, 6, 7, 8, 9])

res_2 = flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]])
print(res_2 == [1, 2, 3, 4, 5, 6, 100])