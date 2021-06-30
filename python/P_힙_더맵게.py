"""
Author: Kim YeongHwa
Date: 2021-06-30
Title: Programmers/힙(Heap)/더 맵게
Language: Python 3
Contents:
    문제 설명
    매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.
    섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
    Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

    제한 사항
    scoville의 길이는 2 이상 1,000,000 이하입니다.
    K는 0 이상 1,000,000,000 이하입니다.
    scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
    모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

    입출력 예
    scoville	K	return
    [1, 2, 3, 9, 10, 12]	7	2

    입출력 예 설명
    스코빌 지수가 1인 음식과 2인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
    새로운 음식의 스코빌 지수 = 1 + (2 * 2) = 5
    가진 음식의 스코빌 지수 = [5, 3, 9, 10, 12]

    스코빌 지수가 3인 음식과 5인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
    새로운 음식의 스코빌 지수 = 3 + (5 * 2) = 13
    가진 음식의 스코빌 지수 = [13, 9, 10, 12]

    모든 음식의 스코빌 지수가 7 이상이 되었고 이때 섞은 횟수는 2회입니다.
"""
# 효율성 테스트 미통과
# from collections import deque
# import bisect

# def solution(scoville, K):
#     answer = 0
#     # list 정렬
#     deq = deque(sorted(scoville))

#     while True:
#         # 최소 스코빌지수가 K보다 작으면 반복
#         if deq[0] >= K:
#             break

#         # list의 첫 번째 원소가 K보다 작으며, list의 길이가 2보다 작으면 해당 list는 -1 반환
#         if len(deq) < 2:
#             answer = -1
#             break

#         first = deq.popleft()
#         second = deq.popleft()
#         temp = first + (second * 2)
#         bisect.insort(deq, temp)
#         answer += 1

#     return answer

import heapq


def solution(scoville, K):
    answer = 0

    # heap sort
    heapq.heapify(scoville)

    while True:
        first = heapq.heappop(scoville)

        if first >= K:
            break
        if len(scoville) < 1:
            answer = -1
            break
        second = heapq.heappop(scoville)

        temp = first + (second * 2)
        heapq.heappush(scoville, temp)
        answer += 1

    return answer

if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    expected = 2
    result = solution(scoville, K)

    if expected == result:
        print("정답입니다.")
    else:
        print("오답입니다.")
    print('Expected: {0}\nResult: {1} '.format(expected, result))