def re(depth):
    if depth == 3:
        return
    for i in range(3):
        re(depth + 1)
        print(depth)

re(0)