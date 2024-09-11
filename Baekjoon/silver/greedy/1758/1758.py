N = int(input())

tip = [None]*N

money = 0

for i in range(N):
    tip[i] = int(input())

tip.sort(reverse=True)

for i in range(N):
    if (tip[i] - i) > 0:
        money += tip[i] - i

print(money)