def solution(numlist, n):
    answer = []
    
    numlist.sort(key=lambda x: (abs(x-n), -x))
    
    return numlist

# https://school.programmers.co.kr/learn/courses/30/lessons/120880?language=python3