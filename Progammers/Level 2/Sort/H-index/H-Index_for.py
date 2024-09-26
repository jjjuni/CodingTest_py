def solution(citations):
    h_index = 0

    citations.sort(reverse=True)

    for _ in range(len(citations)):
        if citations[h_index] < h_index + 1:
            break
        h_index += 1
        
    return h_index