S = list(input())

count = 0

for i in range(len(S) - 1):
    if S[i] == S[0] and S[i+1] != S[0]:
        count += 1

print(count)

# https://kk-programming.tistory.com/9