"""
Author: Kim YeongHwa
Date: 2020-08-10
Title: 9461
Language: Python 3
"""

def make_padovan():
    padovan[0] = 1
    padovan[1] = 1
    padovan[2] = 1

    for i in range(3, 100):
        padovan[i] = padovan[i - 2] + padovan[i - 3]

padovan = [0] * 100
make_padovan()
test_case = int(input())
for _ in range(test_case):
    N = int(input())
    print(padovan[N - 1])



