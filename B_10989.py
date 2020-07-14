"""
Author: Kim YeongHwa
Date: 2020-07-14
Title: 10989
Language: Python 3
"""
import sys

array = [0] * 10001
N = int(input())

for i in range(0, N):
    index = int(sys.stdin.readline())
    array[index] += 1

for i in range(0, 10001):
    if array[i]:
        for j in range(0, array[i]):
            print(i)