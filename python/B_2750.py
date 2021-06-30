"""
Author: Kim YeongHwa
Date: 2020-07-10
Title: 2750
Language: Python 3
"""

def bubble_sort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array) - 1):
            if array[j] >= array[j + 1]:
                temp = array[j + 1]
                array[j + 1] = array[j]
                array[j] = temp
    return array

def insert_sort(array):
    for i in range(1, len(array)):
        for j in range(0, len(array)):
            if array[i] <= array[j]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
    return array


test_case = int(input())
array = []

for i in range(0, test_case):
    array.append(int(input()))

array = insert_sort(array)
for i in range(0, test_case):
    print(array[i])