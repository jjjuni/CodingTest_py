def solution(numbers):
    result = ""
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])

    numbers.sort(reverse=True, key=lambda x: x*4)

    for i in range(len(numbers)):
        result += numbers[i]

    if int(result) == 0:
        return '0'
    return result

numbers = [0, 0, 0]

print(solution(numbers))