"""
Author: Kim YeongHwa
Date: 2020-07-13
Title: 1011
Language: Python 3
"""

def get_count(length):
    square_root = 1
    count = 0
    while True:
        if square_root ** 2 <= length < (square_root + 1) ** 2:
            break
        square_root += 1
    if square_root ** 2 == length:
        count = square_root + square_root - 1
    elif square_root ** 2 < length <= square_root ** 2 + square_root:
        count = square_root + square_root
    elif square_root ** 2 + square_root < length < (square_root + 1) ** 2:
        count = square_root + square_root + 1
    return count

test_case = int(input())
result = []

for i in range(0, test_case):
    x, y = map(int, input().split())
    result.append(get_count(y - x))

for i in range(0, test_case):
    print(result[i])