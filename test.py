def solution(board, moves):
    answer = 0

    basket = list()

    for i in range(0, len(board)):
        if board[i][moves.pop(0)] != 0:
            basket.append(board[i][moves.pop(0) + 1])
            # if basket[len(basket) - 1] is basket[len(basket) - 2]:
            #     basket.pop()
            #     basket.pop()
            #     answer = answer + 1
        else:
            i = i - 1
    return answer

solution()