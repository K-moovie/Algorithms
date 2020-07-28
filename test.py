# import copy
#
#
# count = 0
#
# N = int(input())
# visited = [False for _ in range(N)]
# visited_queue = []
#
#
#
# def is_possible(i):
#     print("isPossible: ", end="")
#     print(visited_queue)
#     visited_queue.append(copy.deepcopy(visited))
#     print("isPossible: " , end="")
#     print(visited_queue)
#     visited[i] = True
#
#
# def dfs(depth):
#     global count
#     global visited
#     if depth == N:
#         count += 1
#         print("count: " + str(count))
#         return
#
#     for i in range(N):
#         if visited[i]:
#             continue
#
#         print(i)
#         is_possible(i)
#
#
#         dfs(depth + 1)
#         visited = copy.deepcopy(visited_queue.pop())
#         print(visited)
#
#
# dfs(0)
# print(count)
#
#
# # a = [True]
# # def b():
# #     a[0] = False
# #     print("B: ", end="")
# #     print(a)
# #
# # def c():
# #     b()
# #     print(a)
# #
# # print(a)
# # c()
# #
# # a.pop()
# # a.pop()

n, ans = int(input()), 0
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)

def solve(i):
    global ans
    if i == n:
        ans += 1
        return
    for j in range(n):
        if not (a[j] or b[i+j] or c[i-j+n-1]):
            a[j] = b[i+j] = c[i-j+n-1] = True
            solve(i+1)
            a[j] = b[i+j] = c[i-j+n-1] = False

solve(0)
print(ans)
