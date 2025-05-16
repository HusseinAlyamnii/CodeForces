dollars = int(input())
num=0

for i in range(dollars):
    if dollars >= 100:
        num += 1
        dollars -= 100
    elif dollars >= 20:
        num += 1
        dollars -= 20
    elif dollars >= 10:
        num += 1
        dollars -= 10
    elif dollars >= 5:
        num += 1
        dollars -= 5
    elif dollars >= 1:
        num += 1
        dollars -= 1
    else:
        break
print(num)
