import sys
sys.setrecursionlimit(10**6)                # 파이썬 기본 재귀 한계 100회 -> 늘려줌


def Search(n, node):                        # 인접리스트(node[])를 탐색하며 부모 노드 정보(Parent[]) 저장
    for i in range(len(node[n])):
        if node_F[node[n][i]] != 1:
            Parent[node[n][i]] = n
            node_F[node[n][i]] = 1
            Search(node[n][i], node)


N = int(input())

node = [[] for _ in range(N+1)]            
node_F = [0]*(N+1)
node_F[1] = 1
Parent = [0]*(N+1)

for _ in range(N-1):                        # 입력 받은 정점 정보를 통해 인접리스트(node[]) 생성
    a, b = map(int, input().split())
                   
    node[b].append(a)
    node[a].append(b)

Search(1, node)

for i in range(2, len(Parent)):
    print(Parent[i])