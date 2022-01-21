import sys
n = int(sys.stdin.readline())

result = 0

length = list(map(int, sys.stdin.readline().split()))

cost = list(map(int, sys.stdin.readline().split()))

for i in range(n-1):
    if cost[i] == min(cost[:n-1]):
        result += cost[i]*sum(length[i:])
        break
    else:
        result += cost[i]*length[i]

print(result)
