def sol():
    pass

def dfs(depth):
    if depth == 8:
        # print(case)
        return

    for i, v in enumerate(visited):
        if not v:
            visited[i] = True
            case[depth] = i
            if depth >= 7:
                print(depth)
            dfs(depth+1)
            visited[i] = False

visited = list(False for _ in range(8))
case = list(range(8))
dfs(0)