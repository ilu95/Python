from sys import stdin

n = int(stdin.readline())

res = []

for i in range(n):
    order = stdin.readline().split()
    if order[0] == "push":
        res.append(order[1])
    if order[0] == "pop":
        if res:
            print(res.pop())
        else:
            print("-1")
    if order[0] == "size":
        print(len(res))
    if order[0] == "empty":
        if res:
            print("0")
        else:
            print("1")
    if order[0] == "top":
        if res:
            print(res[len(res)-1])
        else:
            print("-1")
    order.clear()
