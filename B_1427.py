"""
Author: Kim YeongHwa
Date: 2020-07-17
Title: 1427
Language: Python 3
"""
def get_count(i):
    return array.count(i)

input_value = input()
array = list(input_value)

for i in range(0, len(array)):
    array[i] = int(array[i])

output = ""
for i in reversed(range(10)):
    if get_count(i) != 0:
        for j in range(0, get_count(i)):
            output += str(i)

print(output)