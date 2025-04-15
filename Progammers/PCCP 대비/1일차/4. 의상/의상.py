def solution(clothes):
    
    clothes.sort(key=lambda item: item[1])
    
    arr = [""]
    arr_result = [0]
    
    for item in clothes:
        if arr[-1] != item[1]:
            arr.append(item[1])
            arr_result.append(1)
        else:
            arr_result[-1] += 1
    
    result = 1
    
    for i in arr_result:
        result *= i+1
    
    return result-1


# return ((분류 별 의상 갯수 + 1)을 곱한 수 - 1)

# https://school.programmers.co.kr/learn/courses/30/lessons/42578?language=python3