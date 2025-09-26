direction = [[0, 1], [1, 0]]

def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
        
    for p in puddles:
        dp[p[1]-1][p[0]-1] = -1
        
    for i in range(n):
        for j in range(m):
            if dp[i][j] != -1:  # 현재 위치 웅덩이 X
                if i - 1 >= 0 and dp[i-1][j] != -1:  # y-1 웅덩이 X
                    dp[i][j] += dp[i-1][j]
                if j - 1 >= 0 and dp[i][j-1] != -1:  # x-1 웅덩이 X
                    dp[i][j] += dp[i][j-1]    
            
    return dp[n-1][m-1]%1000000007
    
print(solution(4, 3, [[2, 2]]))