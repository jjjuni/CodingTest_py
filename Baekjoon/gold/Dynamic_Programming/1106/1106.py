C, N = map(int, input().split())

cost = [None] * N
cstm = [None] * N
dp = [None] * (C + 1)
dp[0] = 0

for i in range(N):
    cost[i], cstm[i] = map(int, input().split())

for i in range(N):
    for j in range(C + 1):
        tmp = dp[j - cstm[i] if j > cstm[i] else 0] + cost[i]
        if dp[j] == None or tmp < dp[j]:
            dp[j] = tmp

print(dp[C])