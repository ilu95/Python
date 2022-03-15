from sys import stdin
# N과 M이 주어짐, 8 <= N, M <= 50인 자연수
n, m = map(int, stdin.readline().split())

B_board = [["B", "W", "B", "W", "B", "W", "B", "W"],
           ["W", "B", "W", "B", "W", "B", "W", "B"],
           ["B", "W", "B", "W", "B", "W", "B", "W"],
           ["W", "B", "W", "B", "W", "B", "W", "B"],
           ["B", "W", "B", "W", "B", "W", "B", "W"],
           ["W", "B", "W", "B", "W", "B", "W", "B"],
           ["B", "W", "B", "W", "B", "W", "B", "W"],
           ["W", "B", "W", "B", "W", "B", "W", "B"]]

W_board = [["W", "B", "W", "B", "W", "B", "W", "B"],
           ["B", "W", "B", "W", "B", "W", "B", "W"],
           ["W", "B", "W", "B", "W", "B", "W", "B"],
           ["B", "W", "B", "W", "B", "W", "B", "W"],
           ["W", "B", "W", "B", "W", "B", "W", "B"],
           ["B", "W", "B", "W", "B", "W", "B", "W"],
           ["W", "B", "W", "B", "W", "B", "W", "B"],
           ["B", "W", "B", "W", "B", "W", "B", "W"]]
graph = []
res = []
# 8x8 만큼 비교하는 함수


def check(x, y):
    count_b = 0
    count_w = 0
    start_x = x
    start_y = y
    for i in range(x, x+8):
        for j in range(y, y+8):
            if graph[start_x][start_y] == "B":
                if graph[i][j] != B_board[i-x][j-y]:
                    count_b += 1
                if graph[i][j] != W_board[i-x][j-y]:
                    count_w += 1
            if graph[start_x][start_y] == "W":
                if graph[i][j] != B_board[i-x][j-y]:
                    count_b += 1
                if graph[i][j] != W_board[i-x][j-y]:
                    count_w += 1
    count = min(count_b, count_w)
    res.append(count)


# N개의 줄에 보드의 각 행의 상태가 주어짐, B : 검정 / W : 하양
for i in range(n):
    graph.append(list(stdin.readline()))


# 각 행의 원소를 돌아보며 B,W가 연속적인 구간이 가장 긴 부분 탐색(카운트)
# 8x8 범위를 탐색할건데 보드의 크기가 8x8보다 큰 경우 시작 위치를 기준으로 경우의 수 마다 추가 탐색

for i in range(n):
    # 범위 벗어났을 시
    if i+7 >= n:
        break
    for j in range(m):
        # 범위 벗어났을 시
        if j+7 >= m:
            break
        check(i, j)

print(min(res))
