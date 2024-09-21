import heapq

def solution(scoville, K):
    result = 0
    
    heapq.heapify(scoville)  # scoville 리스트를 힙으로 변환
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        mix = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, mix)
        result += 1

    return result

print(solution([1, 2, 3, 9, 10, 12], 7))