N = int(input())

coin = 0

while N % 5 != 0:               # 5 * n 으로 나누어 질 때 까지 2원짜리 동전 추가
    if N == 1 or N == 3:
        coin = -1
        break
    N -= 2
    coin += 1

if coin != -1:
    coin += (N / 5)

print(int(coin))