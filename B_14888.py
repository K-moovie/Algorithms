"""
Author: Kim YeongHwa
Date: 2020-08-04
Title: 14888
Language: Python 3
"""

def dfs(depth, result):

    if depth == N - 1:
        # print("return")
        result_array.append(result)
        return

    # print(depth)
    old_result = result
    for i in range(N - 1):
        result = old_result
        if not visited[i]:
            visited[i] = True
            # print(result, end="")
            if operator[i] == 0:
                result += array[depth + 1]
                # print('+', end = "")
            elif operator[i] == 1:
                result -= array[depth + 1]
                # print('-', end = "")
            elif operator[i] == 2:
                result *= array[depth + 1]
                # print('*', end = "")
            elif operator[i] == 3:
                result = int(result / array[depth + 1])
            #     print('/', end = "")
            # print(array[depth + 1])
            dfs(depth + 1, result)
            visited[i] = False




N = int(input())
array = list(map(int, input().split()))
operator_list = list(map(int, input().split()))
operator = [i for i in range(4) for _ in range(operator_list[i])]
result_array = []
visited = [False] * (N - 1)
dfs(0, array[0])
# print(*result_array)

print(max(result_array))
print(min(result_array))