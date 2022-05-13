from sys import stdin
from collections import deque

n1, n2 = map(int, stdin.readline().split())

road = [0]*(n1+n2)
count = 0

group1 = deque(list(stdin.readline().strip()))
group2 = deque(list(stdin.readline().strip()))

t = int(stdin.readline())

# 그룹2가 그룹1을 넘어가지는 않은 경우
if t <= n1:
    for i in range(1, n2-t+1):
        road[-i] = group2.pop()
    for i in range(n1-t, len(road), 2):
        if group2:
            road[i] = group2.popleft()
            count += 1
    for i in range(len(road)):
        if road[i] == 0:
            road[i] = group1.pop()
# 그룹 2가 그룹 1을 넘어가기 시작한 경우
elif t > n1:
    over = t-n1+1
    for i in range(over):
        if not group2:
            break
        road[i] = group2.popleft()
    for i in range(over+1, len(road), 2):
        if not group2:
            break
        road[i] = group2.popleft()
    for i in range(len(road)):
        if not group1:
            break
        if road[i] == 0:
            road[i] = group1.pop()

road = ''.join(map(str, road))
print(road)
