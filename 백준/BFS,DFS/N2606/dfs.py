import sys


def dfs(v):
    global answer
    visited[v] = True
    for i in network[v]:
        if not visited[i]:
            answer += 1
            dfs(i)


n = int(input())
m = int(input())
network = [[] for _ in range(n+1)]
visited = [False]*(n+1)
answer = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    network[a].append(b)
    network[b].append(a)

dfs(1)
print(answer)
