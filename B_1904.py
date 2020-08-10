"""
Author: Kim YeongHwa
Date: 2020-08-08
Title: 1904
Language: Python 3
"""

N = int(input())
first = 0
second = 1
if N == second:
    print(second)

else:
    result = 0
    for _ in range(N):
        result = first + second
        first = second
        second = result
    print(result % 15746)