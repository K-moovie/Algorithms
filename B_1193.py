"""
Author: Kim YeongHwa
Date: 2020-07-07
Title: 1193
Language: Python 3
"""

input = int(input())
round = 0
sum = 0
copy = input

while True:
    if input <= sum:
        break
    else:
        round += 1
        sum += round

a = (sum - round)

print("round: " + str(round))
print("sum: " + str(sum))


print(str((round + 1) % a) + "/",  end="")
print(str((round + 1) - a) + "/",  end="")

""""
mod = input % sum

print("round: " + str(round))
print("sum: " + str(sum))
print("mod: " + str(mod))

if round % 2 == 1:
    print(str(round - mod + 1) + "/", end="")
    print(round - (round - mod))

else:
    print(str(round - (round - mod)) + "/", end="")
    print(round - mod + 1)"""