N = int(input())

coin = 0

while N % 5 != 0:
    if N == 1 or N == 3:
        coin = -1
        break
    N -= 2
    coin += 1

if coin != -1:
    coin += (N / 5)

print(int(coin))