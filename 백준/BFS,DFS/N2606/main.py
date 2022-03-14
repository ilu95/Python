from collections import deque
import sys

# 컴퓨터의 수
n = int(input())

# 컴퓨터 쌍의 수
m = int(input())

network = [[] for _ in range(n+1)]
visited = [False]*(n+1)
answer = 0

# 양방향 연결리스트
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    network[a].append(b)
    network[b].append(a)

q = deque()
q.append(1)
visited[1] = True
while q:
    v = q.popleft()
    for i in network[v]:
        if not visited[i]:
            visited[i] = True
            q.append(i)
            answer += 1
print(answer)
