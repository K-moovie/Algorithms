"""
Author: Kim YeongHwa
Date: 2020-07-10
Title: 2751
Language: Python 3
"""
import math
import sys

def insert_heap(array):
    present_index = len(array) - 1
    if present_index == 0:
        return array
    while True:
        if present_index % 2 == 1:
            parent_index = math.floor(present_index / 2)
        else:
            parent_index = math.floor(present_index / 2) - 1

        if array[present_index] <= array[parent_index]:
            array[present_index], array[parent_index] = array[parent_index], array[present_index]
        present_index = parent_index
        if present_index <= 0:
            break
    return array

def delete_heap(array):
    print(array[0])
    last_index = len(array) - 1
    array[0] = array[last_index]
    del array[last_index]
    present_index = 0
    while True:
        min_index = -1
        left_child_index = present_index * 2 + 1
        right_child_index = present_index * 2 + 2
        if len(array) -1 < left_child_index and len(array) -1 < right_child_index:
            break
        elif (len(array) -1 > left_child_index and len(array) -1 < right_child_index) or (len(array) -1 == left_child_index):
            min_index = left_child_index
        elif len(array) -1 >= left_child_index and len(array) -1 >= right_child_index:
            min_index = left_child_index if (array[left_child_index] < array[right_child_index]) else right_child_index

        if array[present_index] >= array[min_index]:
            array[present_index], array[min_index] = array[min_index], array[present_index]
            present_index = min_index
        elif array[present_index] < array[min_index]:
            break
    return array

test_case = int(sys.stdin.readline())
array = []
for i in range(0, test_case):
    array.append(int(sys.stdin.readline()))
    array = insert_heap(array)

for i in range(0, test_case):
    array = delete_heap(array)