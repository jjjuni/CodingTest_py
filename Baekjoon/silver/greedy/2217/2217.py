N = int(input())

rope = [None] * N

max = 0

for i in range(N):
    rope[i] = int(input())

rope.sort(reverse=True)

for i in range(N):                  # 1개의 로프로 들 수 있는 무게부터 시작
    if max < (i + 1) * rope[i]:     # 여러개의 로프로 들었을 때 더 많은 무게를 들 수 있다면 max 에 저장
        max = (i + 1) * rope[i]
    
print(max)