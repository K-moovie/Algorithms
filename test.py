import copy


count = 0

N = int(input())
visited = [False for _ in range(N)]
visited_queue = []



def is_possible(i):
    print("isPossible: ", end="")
    print(visited_queue)
    visited_queue.append(copy.deepcopy(visited))
    print("isPossible: " , end="")
    print(visited_queue)
    visited[i] = True


def dfs(depth):
    global count
    global visited
    if depth == N:
        count += 1
        print("count: " + str(count))
        return

    for i in range(N):
        if visited[i]:
            continue

        print(i)
        is_possible(i)


        dfs(depth + 1)
        visited = copy.deepcopy(visited_queue.pop())
        print(visited)


dfs(0)
print(count)


# a = [True]
# def b():
#     a[0] = False
#     print("B: ", end="")
#     print(a)
#
# def c():
#     b()
#     print(a)
#
# print(a)
# c()
#
# a.pop()
# a.pop()