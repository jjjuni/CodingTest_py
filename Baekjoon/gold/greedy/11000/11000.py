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


# 참고자료 (sort(key))
# https://rnrmffj.tamchart.com/74
# https://gusugi.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-sorted-%ED%95%A8%EC%88%98-%EC%9D%B4%ED%95%B4-%EB%B0%8F-%ED%99%9C%EC%9A%A9%EB%B2%95-key-%EB%A7%A4%EA%B0%9C%EB%B3%80%EC%88%98-%ED%99%9C%EC%9A%A9%EB%B2%95

# 참고자료 (파이썬 heap)
# https://velog.io/@yeonsubaekk/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%9E%99%ED%81%90heapq-%EB%AA%A8%EB%93%88%EB%A1%9C-%ED%9E%99heap-%EB%8B%A4%EB%A3%A8%EA%B8%B0