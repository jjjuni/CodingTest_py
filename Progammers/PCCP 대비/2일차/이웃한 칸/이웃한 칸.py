def solution(board, h, w):
    answer = 0
    
    dh = [0, -1, 1, 0]
    dw = [1, 0, 0, -1]
    
    for i in range(4):
        try:
            if h+dh[i] >= 0 and w+dw[i] >= 0:
                if board[h][w] == board[h+dh[i]][w+dw[i]]:
                    answer += 1
        except: 
            answer = answer
    return answer

# https://campus.programmers.co.kr/tryouts/175742/challenges?language=python3