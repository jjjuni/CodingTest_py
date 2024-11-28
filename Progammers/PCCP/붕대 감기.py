def solution(bandage, health, attacks):
    answer = health
    
    attackTime = [False] * attacks[-1][0]
    for i in range(len(attacks)):
        attackTime[attacks[i][0] - 1] = True
    
    succTime = 0
    
    for i in range(attacks[-1][0]):
        if (attackTime[i]): 
            for j in range(len(attacks)):
                if (attacks[j][0] == i + 1):
                    answer -= attacks[j][1]
                    succTime = 0

        else: 
            succTime += 1
            answer += bandage[1]
            if (succTime == bandage[0]):
                answer += bandage[2]
                succTime = 0
        
        if (answer <= 0):
            return -1
        if (answer > health):
            answer = health
    
    return answer

print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))
print(solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
print(solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
print(solution([1, 1, 1], 5, [[1, 2], [3, 2]]))
