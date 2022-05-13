from sys import stdin

king, stone, n = stdin.readline().split()
n = int(n)

raw_k = int(king[1])
col_k = int(ord(king[0])) - int(ord('A'))

raw_s = int(stone[1])
col_s = int(ord(stone[0])) - int(ord('A'))

# 이동할 수 있는 8가지 방향 정의
# R, L, B, T, RT, LT, RB, LB
direction = ["R", "L", "B", "T", "RT", "LT", "RB", "LB"]
steps = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (1, 1), (1, -1)]

# n번 움직임
for i in range(n):
    # 킹이 움직일 방향을 입력받고 그에 맞게 이동
    move = stdin.readline().rstrip()
    if move in direction:
        for step in steps:
            # 방향에 맞춰 이동 수행
            if steps[direction.index(move)] == step:
                # print("\n\n킹의 현재 위치 :", col_k, raw_k)
                # print("돌의 현재 위치 :", col_s, raw_s)
                # 이동하기 전 킹의 위치 저장 - 이탈 할 경우 복귀 용도
                pre_raw_k = raw_k
                pre_col_k = col_k
                raw_k -= step[0]
                col_k += step[1]
                # 만약 킹이 돌과 같은곳으로 이동하면 돌도 같은 방향으로 한 칸 이동
                # 이동하기 전 돌의 위치 저장 - 이탈 할 경우 복귀 용도
                pre_raw_s = raw_s
                pre_col_s = col_s
                if raw_k == raw_s and col_k == col_s:
                    raw_s -= step[0]
                    col_s += step[1]
                # 킹이나 돌이 체스판 밖으로 나가면 해당 이동은 건너뛰고 다음 이동 수행
                if raw_k < 1 or raw_k > 8 or col_k < 0 or col_k >= 8 or raw_s < 1 or raw_s > 8 or col_s < 0 or col_s >= 8:
                    # print("범위 이탈", raw_k, col_k)
                    raw_k = pre_raw_k
                    col_k = pre_col_k
                    raw_s = pre_raw_s
                    col_s = pre_col_s
                    # print("킹의 이탈 후 위치 :", raw_k, col_k)
                    # print("돌의 이탈 후 위치 :", raw_s, col_s)
                    continue

                # print("킹의 이동 후 위치 :", col_k, raw_k)
                # print("돌의 이동 후 위치 :", col_s, raw_s)


# 킹과 돌의 마지막 위치 출력(입력 방식의 반대로)
print(chr(col_k+int(ord("A"))), raw_k, sep='')
print(chr(col_s+int(ord("A"))), raw_s, sep='')
