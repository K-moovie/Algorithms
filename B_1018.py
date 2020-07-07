"""
Author: Kim YeongHwa
Date: 2020-07-07
Title: 1018
Language: Python 3
"""

def reverse_first(first):
    if first == "W":
        return "B"
    elif first == "B":
        return "W"

def result(chess_board, check):
    count = 0
    first = check
    for i in chess_board:
        for j in i:
            if j != first:
                count += 1
            first = reverse_first(first)
        first = reverse_first(first)
    return count

n, m = map(int, input().split(" "))
total_chess_board = []
count_list = []

for i in range(0, n):
    temp = input()
    total_chess_board.append(temp)

for i in range(0, n-7):
    for j in range(0, m-7):
        temp = []
        for k in range(0, 8):
            temp.append(total_chess_board[i + k][j:j+8])
        count_list.append(result(temp, "W"))
        count_list.append(result(temp, "B"))

print(min(count_list))