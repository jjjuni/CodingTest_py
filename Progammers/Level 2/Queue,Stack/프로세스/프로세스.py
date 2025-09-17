# 내 풀이
# from collections import deque

# def solution(priorities, location):
#     array = list(zip(priorities, [i for i in range(len(priorities))]))
#     deque_array = deque(array)

#     answer = 1

#     while True:
#         max_index = deque_array.index(max(deque_array, key=lambda x: x[0]))
#         for _ in range(max_index):
#             deque_array.append(deque_array.popleft())
        
#         tmp = deque_array.popleft()

#         if tmp[1] == location:
#             return answer
#         answer += 1
#         print(deque_array)

from collections import deque

def solution(priorities, location):
    answer = 0
    array = [(i,p) for i,p in enumerate(priorities)]
    deque_array = deque(array)

    while True:
        tmp = deque_array.popleft()
        if any(tmp[1] < p[1] for p in deque_array):
            deque_array.append(tmp)
        else:
            answer += 1
            if (tmp[0] == location):
                return answer

print(solution([1, 1, 9, 1, 1, 1], 0))