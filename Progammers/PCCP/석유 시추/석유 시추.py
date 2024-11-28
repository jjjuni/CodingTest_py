def solution(land):
    depth = len(land)
    width = len(land[0])

    answer = [0] * width

    for i in range(width):
        landTmp = land
        for j in range(depth):
            answer[i] += getOil(j, i, landTmp, None)
        
    return answer


def getOil(y, x, land, prev):
    oil = 0
    if (land[y][x] == 1):
        land[y][x] = 0
        oil += 1
        if (prev != 'left' and x != 0):
            oil += getOil(y, x-1, land, 'right')
        if (prev != 'right' and x + 1 < len(land)):
            oil += getOil(y, x+1, land, 'left')
        if (prev != 'up' and y != 0):
            oil += getOil(y-1, x, land, 'down')
        if (prev != 'down' and y + 1 < len(land)):
            oil += getOil(y+1, x, land, 'up')
    else:
        return 0
    return oil
    

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))