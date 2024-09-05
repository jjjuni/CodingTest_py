num = int(input())

count = 0

while 1:
    if num >= 3:
        num -= 3
        count += 1
    elif num >= 1:
        num -= 1
        count += 1
    else:
        break

if count % 2 == 1:
    print("SK")
else:
    print("CY")