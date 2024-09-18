N = int(input())

result = 0

for i in range(N):
    string = str(i)
    sum = i
    for j in range(len(string)):
        sum += int(string[j])
    if sum == N:
        result = i
        break

print(result)