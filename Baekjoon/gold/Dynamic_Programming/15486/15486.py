N = int(input())

T = []
P = []
dp = [[-1, 0] for _ in range(N)]
max = 0

for _ in range(N):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)

for i in range(N):
    tmp = dp[i-1][1]
    for j in range(i, N):   
        if j + T[i] - 1 < N:                                                        # 배열 길이 넘지 않도록
            if i > dp[j + T[i] - 1][0]:                                                 # 안 겹치는 상담이라면
                dp[j + T[i] - 1][0] = (i + T[i] - 1)
                dp[j + T[i] - 1][1] += P[i]
            else:                                                                       # 겹치는 상담이라면
                if dp[j + T[i] - 1][1] < tmp + P[i]:                                    # 현재 상담이 더 이득이라면    
                    dp[j + T[i] - 1][0] = (i + T[i] - 1)
                    dp[j + T[i] - 1][1] = tmp + P[i]
        else: 
            break
                
for i in range(N):
    if max < dp[i][1]:
        max = dp[i][1]

print(max)