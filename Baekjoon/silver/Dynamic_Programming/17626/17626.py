square = [0] * 301
dp = [0] * 50001

for i in range(1, 301):
    square[i] = i*i

for i in range(1, 50001):
    if i*i > 50000:
        break
    for j in square:
        if i+j < 50001 and dp[i+j] == 0:
            dp[i+j] = dp[i] + 1
        else:
            break

num = int(input())

print(dp[num])

