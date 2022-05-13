from sys import stdin

# n+1일 후 퇴사 예정
n = int(stdin.readline().strip())
# 상담 일정
plan = [0]
max = 0
for i in range(1, n+1):  # 1부터 n까지
    for j in range(1, i):
        max += j
# 결과값을 저장할 dp 테이블
d = [[0] * 2 for _ in range(max)]
# 기간 체크용
today = 1
start = 1
# 0~n 까지를 1일부터 퇴사날까지로 두고 상담 기간과 금액 파악
for i in range(n):
    plan.append(list(map(int, stdin.readline().split())))

# DP진행(바텀업)
for i in range(1, max):
