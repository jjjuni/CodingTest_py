import sys

N = int(sys.stdin.readline())
town = [[] for _ in range(N)]

pop = 0

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    pop += b
    town[i].append(a)
    town[i].append(b)

town.sort(key = lambda x: (x[0]))               # 마을 순서대로 정렬

half_pop = pop / 2

pop = 0

i = 0

for i in range(len(town)):    
    pop += town[i][1]

    if pop >= half_pop:
        break

print(town[i][0])



# def distance(num):                # 중간 마을부터 시작하여 양쪽 마을과 비교하며 탐색 (시간 초과)
#     result = 0
#     for i in range(N):
#         result += abs((list[num][0] - list[i][0]) * list[i][1])               # abs() : 절댓값 함수

#     return result

# N = int(sys.stdin.readline())

# list = [[] for _ in range(N)]

# for i in range(N):
#     a, b = map(int, sys.stdin.readline().split())
#     list[i].append(a)
#     list[i].append(b)

# i = N // 2

# list.sort(key = lambda x: (x[0]))                       # 마을 순서대로 정렬

# postOfc = 0

# while 1:
#     if i > 0 and distance(i) > distance(i - 1):
#         i = i // 2
#     elif i < N - 1 and distance(i) > distance(i + 1):
#         i += (N - i) // 2
#     else:
#         postOfc = i
#         break

# print(list[postOfc][0])
