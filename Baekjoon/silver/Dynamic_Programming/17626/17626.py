dp = [4] * 50001

for i in range(1, 224):             # 1부터 각 제곱수를 저장 
    if i*i <= 50000:                 
        dp[i*i] = 1                 # 제곱근이 양의 정수(제곱근 하나로 표현 가능한 수)
        
for i in range(1, 50000):
    for j in range(1, 224):
        if i+(j*j) > 50000:
            break
        elif dp[i+(j*j)] > dp[i] + 1:
            dp[i+(j*j)] = dp[i] + 1

num = int(input())

print(dp[num])