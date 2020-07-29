"""
Author: Kim YeongHwa
Date: 2020-07-29
Title: 10872
Language: Python 3
"""

def factorial(N):
    if N == 0:
        return 1

    elif N >= 1:
        return N * factorial(N - 1)


N = int(input())
print(factorial(N))