N, K = map(int, input().split())

coin = [None] * N

result = 0

for i in range(N-1, -1, -1):
    coin[i] = int(input())

for i in range(N):
    if K == 0:
        break
    elif K >= coin[i]:
        result += K//coin[i]
        K = K % coin[i]

print(result)