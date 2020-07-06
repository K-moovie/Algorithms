"""
Author: Kim YeongHwa
Date: 2020-07-06
Title: 2839
Language: Python 3
"""

sugar = int(input())
sugar_count = 0

BIG_SUGAR = 5
SMALL_SUGAR = 3

while sugar > 0:
    if sugar % BIG_SUGAR == 0:
        sugar -= BIG_SUGAR
        sugar_count += 1
    elif sugar % SMALL_SUGAR == 0:
        sugar -= SMALL_SUGAR
        sugar_count += 1
    elif sugar > BIG_SUGAR:
        sugar -= BIG_SUGAR
        sugar_count += 1
    else:
        sugar_count = -1
        break

print(sugar_count)