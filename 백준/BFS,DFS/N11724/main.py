import sys


def dfs(v):
    visited[v] = True
    for i in adj[v]:
        if not visited[i]:
            dfs(i)


# n : 정점 개수, m : 간선 개수
n, m = map(int, sys.stdin.readline().split())

# 최적화를 위한 인접 리스트 활용
adj = [[] for _ in range(n+1)]
visited = [False]*(n+1)
cnt = 0

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

# 1번 부터 n번 까지의 노드 순회하며 방문여부 확인 -> 방문이 안되었다는건 연결 요소가 아니라는 것
for i in range(1, n+1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)
