"""
Author: Kim YeongHwa
Date: 2020-07-15
Title: 2108
Language: Python 3
"""

import sys

def get_middle(array, N):
    middle_index = N // 2 + 1
    sum = 0
    for i in range(-4000, 4001):
        sum += array[i]
        if middle_index <= sum:
            return i

def get_mode(array, N):
    max_val = max(array)
    if array.count(max_val) > 1:
        new_array =[]
        for i in range(-4000, 4001):
            if array[i] == max_val:
                new_array.append(i)
        new_array.remove(min(new_array))
        return min(new_array)
    if array.index(max_val) > 4000:
        return array.index(max_val) - 8001
    else:
        return array.index(max_val)

def get_gap(array, N):
    new_array = []
    for i in range(-4000, 4001):
        if array[i] != 0:
            new_array.append(i)
    return new_array[-1] - new_array[0]

N = int(sys.stdin.readline())
array = [0 for i in range(0, 8001)]
sum = 0

for i in range(0, N):
    index = int(sys.stdin.readline())
    sum += index
    array[index] += 1

print(round(sum / N))
print(get_middle(array, N))
print(get_mode(array, N))
print(get_gap(array, N))
