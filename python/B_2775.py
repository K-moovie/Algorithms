"""
Author: Kim YeongHwa
Date: 2020-07-09
Title: 2775
Language: Python 3
"""

def get_count(floor, room_num):
    sum = 0
    if floor == 0:
        return room_num
    else:
        for i in range(1, room_num + 1):
            sum += get_count(floor - 1, i)
        return sum

test_case = int(input())
result = []
for i in range(0, test_case):
    a = int(input())
    b = int(input())
    result.append(get_count(a, b))

for i in range(0, test_case):
    print(result[i])