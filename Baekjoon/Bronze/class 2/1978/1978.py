N = int(input())

result = 0

num = [1] * 1001
num[0] = 0
num[1] = 0

for i in range(3, 1001):
    for j in range(2, i):
        if i % j == 0:
            num[i] = 0
            break

num_list = list(map(int, input().split()))

for i in num_list:
    if num[i] == 1:
        result += 1

print(result)