from collections import deque
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
        # 처음 토마토 좌표 x,y 에 꺼내고
        x, y = queue.popleft()
        # 현 재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))


# bfs를 수행한 결과 출력
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])


bfs()
print("수행 직 후")
for i in range(n):
    print(graph[i])

# 정답이 담길 변수
result = 0
for i in range(n):
    print(graph[i])

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    # 다 익혔다면 최댓값이 정답
    result = max(result, max(i))

print(result-1)
