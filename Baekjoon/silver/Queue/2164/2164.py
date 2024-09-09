from collections import deque
import sys

N = int(sys.stdin.readline())

Q = deque = deque()

for i in range(1, N+1):
    Q.append(i)

while len(Q) != 1:
    Q.popleft()
    Q.append(Q.popleft())

print(Q[0])