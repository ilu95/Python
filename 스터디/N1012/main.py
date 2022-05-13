from sys import stdin
import sys
sys.setrecursionlimit(100000)

t = int(stdin.readline())

def dfs(x,y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= m or y <= -1 or y >= n:
        # print("범위 초과")
        return False
    # print("dfs위치 -> x :", x,"y :", y)
    # 현재 노드를 아직 방문하지 않았다면
    if graph[y][x] == 1:
        # print("배추 발견 -> x :",x,"y :", y)
        # 해당 노드 방문 처리
        graph[y][x] = 0
        # 상,하,좌,우의 위치도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

for j in range(t):
    m, n, k = map(int, stdin.readline().split())
    # 2차원 리스트의 맵 정보 입력받기
    graph = [[0] * m for _ in range(n)]
    
    for i in range(k):
        x, y = map(int,stdin.readline().split())
        graph[y][x] = 1
        
    result = 0
    for i in range(n):
        for j in range(m):
            # print("현재위치 -> x :", j,"y :", i)
            # 현재 위치에서 DFS 수행
            if dfs(j,i) == True:
                result += 1
    print(result)