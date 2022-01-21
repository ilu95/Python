# 요리시간 T초 입력
t = int(input())

cost = [300, 60, 10]
result = []
for i in cost:
    result.append(t//i)
    t = t % i

if t != 0:
    print(-1)
else:
    for j in result:
        print(j, end=" ")
