n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

count = int(m / (k+1)) * k

print("count 1 : ", count)

count += m % (k+1)

print('count :', count)

result += (count) * first
result += (m-count) * second

# while True:
#   for i in range(k):
#     if m == 0:
#       break
#     result += first
#     m -= 1
#   if m == 0:
#     break
#   result += second
#   m -= 1

print(result)
