from collections import deque

def solution(progresses, speeds):

    answer = []

    deque_progresses = deque(progresses)
    deque_speeds = deque(speeds)

    while deque_progresses:
        for i in range(len(deque_progresses)):
            deque_progresses[i] += deque_speeds[i]
        
        count = 0
        while deque_progresses and deque_progresses[0] >= 100:
            count += 1
            deque_progresses.popleft()
            deque_speeds.popleft()
        if count > 0:
            answer.append(count)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))