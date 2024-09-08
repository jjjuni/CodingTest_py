n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
inv = [n + 1]


for _ in range(m):
    a, b = input().split()
    a = int(a)
    b = int(b)
    graph[a].append(b)
    graph[b].append(a)

friend = graph[1]


for i in graph[1]:
    inv[i] = 1

print(inv)