# Author: Kim YeongHwa
# Date: 2020-06-30
# Title: 10996
# Language: Python 3

input = int(input())
max = input * 2

def odd_star_print(i):
    j = 0;
    while True:
        print("*",end="")
        j += 1
        if i == j:
            print("")
            break
        print(" ",end="")
        j += 1
        if i == j:
            print("")
            break

def even_star_print(i):
    j = 0;
    while True:
        print(" ",end="")
        j += 1
        if i == j:
            print("")
            break
        print("*",end="")
        j += 1
        if i == j:
            print("")
            break

for i in range(0, input):
    odd_star_print(input)
    even_star_print(input)