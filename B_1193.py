"""
Author: Kim YeongHwa
Date: 2020-07-07
Title: 1193
Language: Python 3
"""

input = int(input())
round = 0
mod = 0
copy = input
while True:
    round += 1
    if copy - round <= 0:
        break
    else:
        mod += round
        copy -= round

if round % 2 == 1:
    if input % mod == 0:
        print(str(round) + "/", end="")

    print(round - (input%mod))

else:
    if input % mod == 0:
        print(str(round) + "/", end="")
    print(round - (input%mod))