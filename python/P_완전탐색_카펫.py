"""
Author: Kim YeongHwa
Date: 2021-07-12
Title: Programmers/완전탐색/카펫
Language: Python 3
Contents:
    문제 설명
    Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

    Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

    Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

    제한사항
    갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
    노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
    카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

    입출력 예
    brown	yellow	return
    10	    2	    [4, 3]
    8	    1	    [3, 3]
    24	    24	    [8, 6]

"""


def solution(brown, yellow):
    answer = []
    cases = list()

    # yellow의 크기를 기반으로 한 경우의 수들을 생성
    for h in range(1, yellow + 1):
        if yellow % h == 0:
            w = yellow // h
            if w < h:
                break
            cases.append((w, h))

    for case in cases:
        w = case[0]
        h = case[1]

        area = (2 * h) + (2 + w) * 2
        if area == brown:
            answer = list([w + 2, h + 2])
            break
    return answer


if __name__ == '__main__':
    brown = 24
    yellow = 24
    expected = [8, 6]
    result = solution(brown, yellow)

    if expected == result:
        print("정답입니다.")
    else:
        print("오답입니다.")
    print('Expected: {0}\nResult: {1} '.format(expected, result))
