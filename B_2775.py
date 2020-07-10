"""
Author: Kim YeongHwa
Date: 2020-07-09
Title: 2775
Language: Python 3
"""

def get_count(floor, room_num):
    sequence = floor
    sum = 1
    for i in range(0, room_num):

        print("sum:"+ str(sum))
        print("수열:" + str(sequence))
        sum += sequence
        sequence += 1
    return sum


test_case = int(input())
result = []
for i in range(0, test_case):
    a = int(input())
    b = int(input())
    result.append(get_count(a, b))

for i in range(0, test_case):
    print(result[i])