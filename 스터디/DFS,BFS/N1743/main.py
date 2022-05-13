from sys import stdin
import sys
sys.setrecursionlimit(100000)

n, m, k = map(int, stdin.readline().split())
graph = [[0]*m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
result = 0
array = []


def DFS(x, y, cnt):
    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 주어진 범위를 벗어나는 경우 즉시 종료
        if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
            # print("범위 초과")
            continue
        # 현재 노드를 아직 방문하지 않았다면
        if graph[nx][ny] == 1:
            # 해당 노드 방문 처리 후 카운트 1 증가
            cnt = max(cnt, DFS(nx, ny, cnt+1))
    return cnt


for i in range(k):
    r, c = map(int, stdin.readline().split())
    graph[r-1][c-1] = 1

for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if graph[i][j] == 1:
            array.append(DFS(i, j, 1))

print(max(array))
