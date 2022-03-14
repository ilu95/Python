import sys

t = int(input())

for _ in range(t):
    n = int(input())  # 1<= n <= 100,000
    lst = sorted([list(map(int, sys.stdin.readline().strip().split()))
                 for x in range(n)], key=lambda x: x[0])
    cnt = 1
    min = lst[0][1]

    for i in range(1, n):
        if lst[i][1] < min:
            min = lst[i][1]
            cnt += 1
    print(cnt)
