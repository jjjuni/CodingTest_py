def upHeap(arr, index):
    while index > 0:
        parent = (index-1)//2
        if arr[index] >= arr[parent]:
            break
        arr[index], arr[(index-1)//2] = arr[(index-1)//2], arr[index]
        index = parent    

def downHeap(arr, index):

    size = len(arr)

    while (index * 2 + 1) < size:
        child = index * 2 + 1
        if child + 1 < size and arr[child + 1] < arr[child]:
            child += 1

        if arr[index] <= arr[child]:
            break

        arr[index], arr[child] = arr[child], arr[index]
        index = child

def heapPush(arr, item):
    arr.append(item)
    upHeap(arr, len(arr)-1)

def heapPop(arr):
    if len(arr) == 1:
        return arr.pop()
    tmp = arr[0]
    arr[0] = arr.pop()
    downHeap(arr, 0)
    return tmp

def solution(scoville, K):
    result = 0
    scoville.sort()
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        mix = heapPop(scoville) + (heapPop(scoville) * 2)
        heapPush(scoville, mix)
        result += 1

    return result
    
print(solution([1, 2, 3, 9, 10, 12], 7))