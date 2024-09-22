def solution(numbers):
    result = ""
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])

    numbers.sort(reverse=True, key=lambda x: (x[0], x[1%len(x)], x[2%len(x)], x[3%len(x)]))

    for i in range(len(numbers)):
        result += numbers[i]
    
    if int(result) == 0:
        return '0'
    return result