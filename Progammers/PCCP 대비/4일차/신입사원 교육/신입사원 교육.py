import heapq

def solution(ability, number):
    answer = 0
    
    ability.sort()
    
    heap = []
    for i in ability:
        heapq.heappush(heap, i)
    
    for i in range(number):
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a+b)
        heapq.heappush(heap, a+b)
    
    for i in heap:
        answer += i
    
    return answer

# https://campus.programmers.co.kr/tryouts/176089/challenges?language=python3