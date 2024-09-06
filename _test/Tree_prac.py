n = 5

tree = [[] for _ in range(n+1)]

edges = [
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 5)
]

for parent, child in edges:
    tree[parent].append(child)

for i in range(1, n+1):
    print(f"노드 {i}의 자식들 : {tree[i]}")