s = int(input())
n = 0
count = 0
for i in range(1, s+1):
    count += 1
    n += i
    if(n > s):
        count -= 1
        break

print(count)
