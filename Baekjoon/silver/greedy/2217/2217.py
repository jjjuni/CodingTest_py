N = int(input())

rope = [None] * N

max = 0

for i in range(N):
    rope[i] = int(input())

rope.sort(reverse=True)

for i in range(N):
    if max < (i + 1) * rope[i]:
        max = (i + 1) * rope[i]
    
print(max)