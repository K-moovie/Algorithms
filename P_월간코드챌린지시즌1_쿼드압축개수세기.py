"""
Author: Kim YeongHwa
Date: 2021-03-18
Title: Programmers/월간코드챌린지시즌1/쿼드압축 후 개수 세기
Language: Python 3
Contents:
    문제 설명
    0과 1로 이루어진 2n x 2n 크기의 2차원 정수 배열 arr이 있습니다. 당신은 이 arr을 쿼드 트리와 같은 방식으로 압축하고자 합니다. 구체적인 방식은 다음과 같습니다.

    당신이 압축하고자 하는 특정 영역을 S라고 정의합니다.
    만약 S 내부에 있는 모든 수가 같은 값이라면, S를 해당 수 하나로 압축시킵니다.
    그렇지 않다면, S를 정확히 4개의 균일한 정사각형 영역(입출력 예를 참고해주시기 바랍니다.)으로 쪼갠 뒤, 각 정사각형 영역에 대해 같은 방식의 압축을 시도합니다.
    arr이 매개변수로 주어집니다. 위와 같은 방식으로 arr을 압축했을 때, 배열에 최종적으로 남는 0의 개수와 1의 개수를 배열에 담아서 return 하도록 solution 함수를 완성해주세요.

    제한사항
    arr의 행의 개수는 1 이상 1024 이하이며, 2의 거듭 제곱수 형태를 하고 있습니다. 즉, arr의 행의 개수는 1, 2, 4, 8, ..., 1024 중 하나입니다.
    arr의 각 행의 길이는 arr의 행의 개수와 같습니다. 즉, arr은 정사각형 배열입니다.
    arr의 각 행에 있는 모든 값은 0 또는 1 입니다.

    입출력 예
    arr	result
    [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]	[4,9]
    [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]	[10,15]

    입출력 예 설명
    입출력 예 #1
    최종 압축 결과에 0이 4개, 1이 9개 있으므로, [4,9]를 return 해야 합니다.

    입출력 예 #2
    최종 압축 결과에 0이 10개, 1이 15개 있으므로, [10,15]를 return 해야 합니다.
"""
def solution(arr):
    global array
    global answer

    array = arr
    answer = [0, 0]

    check(0, 0, len(arr))

    return answer


def check(x, y, length):
    global array
    global answer
    temp = [0, 0]

    # 재귀함수 탈출 조건
    if length == 1:
        item = array[x][y]
        answer[item] += 1
        return

    mid = length // 2

    # 4분할된 배열의 값을 읽어 temp 배열에 기록한다.
    for i in range(x, x + length):
        for j in range(y, y + length):
            item = array[i][j]
            temp[item] += 1

    # 4분할된 배열 중 한 구역이 모두 1으로 이루어져 았을 때
    if temp[0] == 0:
        answer[1] += 1

    # 4분할된 배열 중 한 구역이 모두 0으로 이루어져 았을 때
    elif temp[1] == 0:
        answer[0] += 1

    # 4분할된 배열 중 한 구역이 0, 1로 이루어져 있을 때
    # 재귀함수를 호출하여 다시 4분할한다.
    else:
        check(x, y, mid)
        check(x + mid, y, mid)
        check(x, y + mid, mid)
        check(x + mid, y + mid, mid)


if __name__ == '__main__':
    arr = [[1, 1, 1, 1, 1, 1, 1, 1],
           [0, 1, 1, 1, 1, 1, 1, 1],
           [0, 0, 0, 0, 1, 1, 1, 1],
           [0, 1, 0, 0, 1, 1, 1, 1],
           [0, 0, 0, 0, 0, 0, 1, 1],
           [0, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 1, 0, 0, 1],
           [0, 0, 0, 0, 1, 1, 1, 1]]

    print('Expected: {0}\nResult: [10, 15]'.format(solution(arr)))