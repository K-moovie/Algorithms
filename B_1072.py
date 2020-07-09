"""
Author: Kim YeongHwa
Date: 2020-07-08
Title: 1072
Language: Python 3
"""

"""I haven't solved this problem yet."""
import sys
sys.setrecursionlimit(100000)

def get_rate(x, y):
    return int((y / x) * 100)

total_round, win = map(int, input().split(" "))
initial_rate = get_rate(total_round, win)

def binary_recursive(target):
    target_rate = get_rate(target, win + (target - total_round))
    if initial_rate > target_rate:
        min = int(target/4)
        binary_recursive(target-min)
    elif initial_rate == target_rate:
        return target - total_round
    elif initial_rate < target_rate:
        binary_recursive(int(target/2))
    else:
        print("error")

print(binary_recursive(10000))
