import string
import numpy as np
# N과 M이 주어짐, 8 <= N, M <= 50인 자연수
n, m = map(int, input().split())

B_board = np.array([["B", "W", "B", "W", "B", "W", "B", "W"],
                    ["W", "B", "W", "B", "W", "B", "W", "B"],
                    ["B", "W", "B", "W", "B", "W", "B", "W"],
                    ["W", "B", "W", "B", "W", "B", "W", "B"],
                    ["B", "W", "B", "W", "B", "W", "B", "W"],
                    ["W", "B", "W", "B", "W", "B", "W", "B"],
                    ["B", "W", "B", "W", "B", "W", "B", "W"],
                    ["W", "B", "W", "B", "W", "B", "W", "B"]])

W_board = np.array([["W", "B", "W", "B", "W", "B", "W", "B"],
                    ["B", "W", "B", "W", "B", "W", "B", "W"],
                    ["W", "B", "W", "B", "W", "B", "W", "B"],
                    ["B", "W", "B", "W", "B", "W", "B", "W"],
                    ["W", "B", "W", "B", "W", "B", "W", "B"],
                    ["B", "W", "B", "W", "B", "W", "B", "W"],
                    ["W", "B", "W", "B", "W", "B", "W", "B"],
                    ["B", "W", "B", "W", "B", "W", "B", "W"]])

# N개의 줄에 보드의 각 행의 상태가 주어짐, B : 검정 / W : 하양
graph = []

for i in range(n):
    graph.append(list(input()))

data = np.empty((0, 8))
min_B = 9999
min_W = 9999
res = 9999
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
        for x in range(i, i+8):
            for y in range(j, j+8):

                # 각 경우의 수를 비교하여 최소 결과를 출력
