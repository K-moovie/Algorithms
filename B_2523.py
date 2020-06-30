a = int(input())
max = a*2

for i in range(1, max):
    if i >= a:
        print("*"*(max-i))
    else:
        print("*"*i)