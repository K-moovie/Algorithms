"""
Author: Kim YeongHwa
Date: 2021-02-27
Title: Programmers/2019 카카오 개발자 겨울 인턴쉽/크레인 인형뽑기 게임
Language: Python 3
"""

def solution(board, moves):
    answer = 0
    basket = list()
    row = 0

    for move in moves:
        pick = move - 1
        for row in range(0, len(board)):
            # item이 해당 행에 존재할 때
            item = board[row][pick]
            if item != 0:
                board[row][pick] = 0
                basket.append(item)
                if len(basket) > 1 and basket[-1] == basket[-2]:
                    # 터진 인형의 갯수
                    basket.pop()
                    basket.pop()
                    answer = answer + 2

                break
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
result = solution(board, moves)
print(result)