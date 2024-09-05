dp = [0] * 5001

dp[3] = 1
dp[4] = -1
dp[5] = 1

for i in range(6, 5001):

    if dp[i-5] > 0:
        dp[i] = dp[i-5] + 1
    elif dp[i-3] > 0:
        dp[i] = dp[i-3] + 1
    else: 
        dp[i] = -1

kg = int(input())       # kg => 3 ~ 5000

print(dp[kg])