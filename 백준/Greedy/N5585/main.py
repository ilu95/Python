money = int(input())
pay = 1000-money

# 잔돈을 리스트로

count = 0
while pay:
    if pay - 500 >= 0:
        count += 1
        pay -= 500
    elif pay - 100 >= 0:
        count += 1
        pay -= 100
    elif pay - 50 >= 0:
        count += 1
        pay -= 50
    elif pay - 10 >= 0:
        count += 1
        pay -= 10
    elif pay - 5 >= 0:
        count += 1
        pay -= 5
    elif pay - 1 >= 0:
        count += 1
        pay -= 1

print(count)
