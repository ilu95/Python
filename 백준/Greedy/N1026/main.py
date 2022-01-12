# 길이가 N
n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum = 0

for _ in range(n):
    sum += min(A)*max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

print(sum)
