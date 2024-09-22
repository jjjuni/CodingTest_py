N = int(input())

arr = list(input().strip())

for i in range(len(arr)):
    arr[i] = ord(arr[i]) - ord('a') + 1

result = 0

for i in range(len(arr)):
    result += arr[i] * (31 ** i)

print(result % 1234567891)