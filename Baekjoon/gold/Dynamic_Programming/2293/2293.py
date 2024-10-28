N, K = map(int, (input().split()))

coin = []
dp = [0] * 10001
dp[0] = 1

for i in range(N):
    coin.append(int(input()))

for i in coin:
    for j in range(i, K + 1):
        dp[j] += dp[j - i]

print(dp[K])