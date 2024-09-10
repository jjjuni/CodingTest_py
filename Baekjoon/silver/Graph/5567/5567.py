def invite(num, index):                 # index : 현재 재귀 중첩
    if index > 2:
        return 0
    else:
        for i in graph[num]:
            inv[num] = 1
            invite(i, index+1)

n = int(input())
m = int(input())

result = 0

graph = [[] for _ in range(n + 1)]
inv = [0]*(n+1)


for _ in range(m):
    a, b = input().split()
    a = int(a)
    b = int(b)
    graph[a].append(b)
    graph[b].append(a)

friend = graph[1]

invite(1, 0)

for i in inv[2:]:
    if i == 1:
        result += 1

print(result)