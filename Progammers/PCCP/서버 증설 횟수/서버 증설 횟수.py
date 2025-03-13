def solution(players, m, k):
    answer = 0

    server = [0] * len(players)

    for i in range(len(players)):
        while players[i] > m * (server[i]+1) - 1:
            answer += 1
            for j in range(k):
                if j + i < len(players):
                    server[i+j] += 1

    return answer

print(solution([0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 1, 1))

#https://school.programmers.co.kr/learn/courses/30/lessons/389479?language=python3