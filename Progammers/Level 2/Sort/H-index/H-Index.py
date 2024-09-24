def solution(citations):
    h_index = 0

    citations.sort(reverse=True)

    while 1:
        if h_index >= len(citations) or citations[h_index] < h_index + 1:
                break
        h_index += 1

    return h_index