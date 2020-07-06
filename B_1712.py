"""
Author: Kim YeongHwa
Date: 2020-06-30
Title: 1712
Language: Python 3
"""

fixed_cost, variable_cost, selling_cost = map(int, input().split(" "))
BREAK_EVEN_COST = 0

if selling_cost <= variable_cost:
    BREAK_EVEN_COST = -1
else:
    BREAK_EVEN_COST = fixed_cost//(selling_cost - variable_cost) + 1
    #//는 몫 연산자
print(BREAK_EVEN_COST)
