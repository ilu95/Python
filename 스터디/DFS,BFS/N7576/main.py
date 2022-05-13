from collections import deque
from re import L
from sys import stdin

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

m, n = map(int, stdin.readline().split())
graph = list()

for i in range(n):
    graph.append(list(map(int, stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()


def bfs():
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현 재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 안익은 토마토 있으면 익힘
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))


# bfs를 수행한 결과 출력
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])

# bfs 수행
bfs()

# 하나라도 익지 않은 토마토가 있으면 -1 출력
if any(0 in i for i in graph):
    print(-1)
else:
    print(max(map(max, graph))-1)
