N = int(input())

A = list(map(int, input().split()))

S = int(input())
    
index = 0

while S > 0:
    if index >= len(A):         # S가 남았지만(바꿀 횟수가 남았지만) 이미 사전순 가장 뒷서는 배열일 경우 탈출
        break
    max = A[index]
    max_i = index
    for i in range(index + 1, S + 1 + index if len(A) > S + 1 + index else len(A)):
        if max < A[i]:
            max = A[i]
            max_i = i

    if index != max_i:
        for i in range(max_i, index, -1):
            A[i], A[i - 1] = A[i - 1], A[i]
            S -= 1
        
    index += 1

for i in range(len(A)):
    print(A[i], end=" ")