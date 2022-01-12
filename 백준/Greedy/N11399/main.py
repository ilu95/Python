# 사람의 수
n = int(input())

p = list(map(int, input().split()))
p.sort()
sum = 0
time = 0

for i in p:
    time += i
    sum += time

print(sum)
