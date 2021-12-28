"""
Author: Kim YeongHwa
Date: 2021-12-28
Title: Programmers/깊이/너비 우선 탐색(DFS/BFS)/네트워크
Language: Python 3
Contents:
    문제 설명
    네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

    컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

    제한사항
    컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
    각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
    i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
    computer[i][i]는 항상 1입니다.
    입출력 예
    n	computers	return
    3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
    3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1
    입출력 예 설명
    예제 #1
    아래와 같이 2개의 네트워크가 있습니다.
    image0.png

    예제 #2
    아래와 같이 1개의 네트워크가 있습니다.

"""


def solution(n, computers):
    answer = []
    link = [[] for _ in range(n)]
    visited = [False] * n
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 0:
                continue

            link[i].append(j)

    def dfs(v, network):
        if visited[v]:
            return []
        visited[v] = True
        network.append(v)
        for i in link[v]:
            if not visited[i]:
                dfs(i, network)
        return network

    for i in range(n):
        temp = dfs(i, [])
        answer.append(temp) if len(temp) > 0 else 0
    return len(answer)


if __name__ == '__main__':
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    expected = 2
    result = solution(n, computers)

    if expected == result:
        print("정답입니다.")
    else:
        print("오답입니다.")
    print('Expected: {0}\nResult: {1} '.format(expected, result))

