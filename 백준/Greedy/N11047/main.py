# 가지고 있는 동전의 종류 N, 목표 금액 K 입력
n, k = map(int, input().split())
A = []

for i in range(n):
    A.append(int(input()))

count = 0
for j in reversed(range(n)):
    count += (k//A[j])
    k = (k % A[j])
print(count)
