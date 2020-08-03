"""
Author: Kim YeongHwa
Date: 2020-07-30
Title: 2580
Language: Python 3
"""


def make_candidate(row, col):
    candidate = []
    for i in range(1, MAX + 1):
        if i not in sudoku_list[row]:
            candidate.append(i)
    for i in range(MAX):
        if sudoku_list[i][col] in candidate:
            candidate.remove(sudoku_list[i][col])
    row_range = range((row // 3) * 3, ((row // 3) * 3) + 3)
    col_range = range((col // 3) * 3, ((col // 3) * 3) + 3)
    for i in row_range:
        for j in col_range:
            if sudoku_list[i][j] in candidate:
                candidate.remove(sudoku_list[i][j])

    return candidate


def sudoku(depth):
    global flag

    if flag:
        return

    if depth == len(zeros):
        for i in sudoku_list:
            print(*i)
        flag = True
        return

    else:
        (i, j) = zeros[depth]
        candidate = make_candidate(i, j)
        for k in candidate:
            sudoku_list[i][j] = k
            sudoku(depth + 1)
            sudoku_list[i][j] = 0


# 변수 선언
MAX = 9
sudoku_list = []

# 9*9 스도쿠 입력
for _ in range(MAX):
    sudoku_list.append(list(map(int, input().split())))

# 0인 원소 좌표 저장
zeros = [(i, j) for i in range(MAX) for j in range(MAX) if sudoku_list[i][j] == 0]
flag = False
sudoku(0)

# test case:
# 0 2 0 9 0 5 0 0 0
# 5 9 0 0 3 0 2 0 0
# 7 0 0 6 0 2 0 0 5
# 0 0 9 3 5 0 4 6 0
# 0 5 4 0 0 0 7 8 0
# 0 8 3 0 2 7 5 0 0
# 8 0 0 2 0 9 0 0 4
# 0 0 5 0 4 0 0 2 6
# 0 0 0 5 0 3 0 7 0
#
# answer: (check it)
# +-----+-----+-----+
# |3 2 1|9 7 5|6 4 8|
# |5 9 6|8 3 4|2 1 7|
# |7 4 8|6 1 2|9 3 5|
# +-----+-----+-----+
# |1 7 9|3 5 8|4 6 2|
# |2 5 4|1 9 6|7 8 3|
# |6 8 3|4 2 7|5 9 1|
# +-----+-----+-----+
# |8 1 7|2 6 9|3 5 4|
# |9 3 5|7 4 1|8 2 6|
# |4 6 2|5 8 3|1 7 9|
# +-----+-----+-----+
