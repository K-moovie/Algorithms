"""
Author: Kim YeongHwa
Date: 2020-07-09
Title: 1193
Language: Python 3
"""

input = int(input())
round = 0
sum = 0
copy = input

while True:
    if input > sum:
        round += 1
        sum += round
    else:
        sum -= round
        break

total = round + 1
#분자
numerator = 0
#분모
denominator = 0

if round % 2 == 0:
    numerator = input - sum
    denominator = total - numerator
else:
    denominator = input - sum
    numerator = total - denominator

print(str(numerator) + "/" + str(denominator))
