import sys
from collections import deque

str = ""

N = int(sys.stdin.readline())
A = sys.stdin.readline().split()
B = sys.stdin.readline().split()

queuestack = deque()

for i in range(N-1, -1, -1):
    if A[i] == '0':                     # 스택은 push 한 값 그대로 pop 하기 배제하고 작성
        queuestack.append(B[i])         # 남은 큐들을 이어붙이면 또 다른 큐가 됨

M = int(sys.stdin.readline())
C = sys.stdin.readline().split()

for i in range(M):
    queuestack.append(C[i])
    tmp = queuestack.popleft()

    if i != 0:
        str += (" " + tmp)
    else:
        str = tmp

print(str)