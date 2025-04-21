def dfs(numbers, target, num_sum, index):
    if len(numbers) == index:
        return 1 if num_sum == target else 0
    return (
        dfs(numbers, target, num_sum + numbers[index], index + 1) + dfs(numbers, target, num_sum - numbers[index], index + 1))

def solution(numbers, target):
    
    return dfs(numbers, target, 0, 0)
    
# https://campus.programmers.co.kr/tryouts/175957/challenges?language=python3