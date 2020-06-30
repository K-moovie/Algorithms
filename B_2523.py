# Author: Kim YeongHwa
# Date: 2020-06-30
# Title: 10996
# Language: Python 3

a = int(input())
max = a*2

for i in range(1, max):
    if i >= a:
        print("*"*(max-i))
    else:
        print("*"*i)