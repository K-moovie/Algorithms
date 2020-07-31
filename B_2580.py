"""
Author: Kim YeongHwa
Date: 2020-07-30
Title: 2580
Language: Python 3
"""

def make_row_candidate(row, col):
    candidate = []
    for i in range(MAX):
        if i not in sudoku_list[row]:
            candidate.append(i)

        if i != sudoku_list[i][col]:
            candidate.append(i)
    return candidate

def make_col_candidate(col):
    col_candidate = []
    for i in range(MAX):
        if i != sudoku_list[i][col]:
            col_candidate.append(i)
    return col_candidate


def sudoku(depth, i, j):
    if depth == 3:
        return

    elif depth == 0:
        row_candidate = make_row_candidate(i)
        for k in range(len(row_candidate)):
            sudoku_list[i][j] = row_candidate[k]
            sudoku(depth + 1, i, j)
    elif depth == 1:
        col_candidate = make_col_candidate(j)
        for k in range(len(col_candidate)):
            sudoku_list[i][j] = col_candidate[k]
            sudoku(depth + 1, i, j)





# 변수 선언
MAX = 9
sudoku_list = []

# 9*9 스도쿠 입력
for _ in range(MAX):
    sudoku_list.append(list(map(int, input().split())))

for i in range(1, MAX):
    for j in range(MAX):
        if sudoku_list[i][j] == 0:
            sudoku(0, i, j)
print(sudoku_list)

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
