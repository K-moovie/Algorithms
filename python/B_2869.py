"""
Author: Kim YeongHwa
Date: 2020-07-09
Title: 2869
Language: Python 3
"""

import math

up_length, down_length, height = map(int, input().split(" "))

move_length = up_length - down_length

height -= up_length

print(math.ceil(height/move_length) + 1)