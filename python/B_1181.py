"""
Author: Kim YeongHwa
Date: 2020-07-20
Title: 1181
Language: Python 3
"""

import sys
def sort(array):
    for i in range(len(array)):
        str_array[i] = list(array[i])
        str_array[i].sort()

N = int(input())
str_array = [[] for i in range(51)]

# 입력을 Counting Sort로 정렬
for i in range(0, N):
    str_item = input()
    str_array[len(str_item)].append(str_item)

# 중복 값 제거를 위한 set 자료형 변환
for i in range(51):
    str_array[i] = set(str_array[i])
sort(str_array)

for i in range(len(str_array)):
    for j in range(len(str_array[i])):
        print(str_array[i][j])