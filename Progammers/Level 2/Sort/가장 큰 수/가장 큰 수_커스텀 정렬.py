from functools import cmp_to_key

def cmp(x, y):
    if x+y > y+x:
        return -1
    elif x+y < y+x:
        return 1
    else:
        return 0
    
def solution(numbers):
    result = ""
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])

    numbers.sort(key=cmp_to_key(cmp))

    for i in range(len(numbers)):
        result += numbers[i]
    
    if int(result) == 0:
        return '0'
    return result