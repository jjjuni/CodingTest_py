import sys
import heapq

N = int(sys.stdin.readline())

inf = [[] for _ in range(N)]

heap = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())

    inf[i].append(a)
    inf[i].append(b)

inf.sort(key=lambda x: (x[0]))                      # 종료시간 순으로 정렬

heapq.heappush(heap, inf[0][1])                     # heap에 첫번째 강의 종료시간 push

for i in range(1, N):
    tmp = heapq.heappop(heap)
    if inf[i][0] >= tmp:
        heapq.heappush(heap, inf[i][1])
    else:
        heapq.heappush(heap, inf[i][1])
        heapq.heappush(heap, tmp)

print(len(heap))

#-------------------------------------------------------------

# 1. 큐(덱) 사용 [시간 초과]
# inf.sort(key=lambda x: (x[0], x[1]))            # Timsort   O(n log n)

# inf = deque(inf)

# i = 0
# while i < len(inf) - 1:
#     flag = True
#     j = i + 1
#     while j < len(inf):
#         if inf[i][1] <= inf[j][0]:
#             inf.popleft()
#             flag = False
#             break
#         else:
#             j += 1

#     if flag:
#         i += 1

# print(len(inf))

#-------------------------------------------------------------

# 2중 for문 [시간초과]
# i = 0
# index = 0
# for i in range(N):
#     if not result:                
#         result.append(inf[i])
#     else:
#         flag = False
#         for j in range(len(result)):
#             if (result[j][0] >= inf[i][1]) or (inf[i][0] >= result[j][1]):
#                 result[j][1] = inf[i][1]
#                 flag = True
#                 break
#         if not flag:
#             result.append(inf[i])

# print(len(result))
