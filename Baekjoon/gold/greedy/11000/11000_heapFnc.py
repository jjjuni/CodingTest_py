import sys

def upHeap(heap, index):
    if index > 1:
        if heap[index] < heap[index//2]:
            tmp = heap[index]
            heap[index] = heap[index//2]
            heap[index//2] = tmp
            upHeap(heap, index//2)

def downHeap(heap, index):
    if index*2 < len(heap):
        child_index = index*2    
        if index*2+1 < len(heap):
            if heap[index*2] > heap[index*2+1]:
                child_index = index*2+1    
        if heap[index] > heap[child_index]:
            tmp = heap[index]
            heap[index] = heap[child_index]
            heap[child_index] = tmp
            downHeap(heap, child_index)

def heapPush(heap, item):
    heap.append(item)
    upHeap(heap, len(heap) - 1)
    

def heapPop(heap):
    if len(heap) > 1:
        heap[1] = heap[-1]
        heap.pop()
        downHeap(heap, 1)

N = int(sys.stdin.readline())

inf = [[] for _ in range(N)]

heap = [None]

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())

    inf[i].append(a)
    inf[i].append(b)

inf.sort(key=lambda x: (x[0]))                      # 시작시간 순으로 정렬

heapPush(heap, inf[0][1])                           # heap에 첫번째 강의 종료시간 push

for i in range(1, N):
    if inf[i][0] >= heap[1]:
        heapPop(heap)
        heapPush(heap, inf[i][1])
    else:
        heapPush(heap, inf[i][1])

print(len(heap)-1)