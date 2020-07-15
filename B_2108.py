"""
Author: Kim YeongHwa
Date: 2020-07-15
Title: 2108
Language: Python 3
"""

import sys
import math

def get_middle(array, N):
    count = -1
    target_index = math.ceil(N / 2)
    for i in range(0, len(array)):
        for j in i:
            if count == target_index:
                return array[i][j]
            count += 1

def get_mode(array):
    new_array = []
    for i in range(0, len(array)):
        new_array.append(len(array[i]))

    min = min(new_array)
    if new_array.count(min) > 1:
        print(4)

sum = 0
array = [[] for i in range(8001)]
N = int(sys.stdin.readline())
for i in range(0, N):
    input = int(sys.stdin.readline())
    array[input].append(input)
    sum += input

new_array = []
for i in range(0, len(array)):
    if array[i]:
        new_array.append(array[i])




print(math.ceil(sum/N))

