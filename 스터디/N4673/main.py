data = list(range(1, 10001))
trash = []

for i in range(1, 10000):
    if i < 10:
        n = i+i
        trash.append(n)
    elif i < 100:
        n = i+int(i / 10)+int(i % 10)
        trash.append(n)
    elif i < 1000:
        n = i+int(i / 100)+int((i / 10) % 10)+int(i % 10)
        trash.append(n)
    elif i < 10000:
        n = i+int(i / 1000)+int((i / 100) % 10)+int((i / 10) % 10)+int(i % 10)
        trash.append(n)

set_data = set(data)
set_trash = set(trash)
res = set_data.difference(set_trash)
res = list(res)
res.sort()

for i in range(len(res)):
    print(res[i])
