def solution(command):
    
    position = [0, 0]
    
    direction = 0
    dh = [1, 0, -1, 0]
    dw = [0, 1, 0, -1]
    
    command_arr = list(command)
    
    for d in command_arr:
        if d == "G":
            position[0] += dw[direction]
            position[1] += dh[direction]
            
        elif d == "B":
            position[0] += dw[direction-2]
            position[1] += dh[direction-2]
        
        elif d == "R":
            direction += 1
            if direction >= 4:
                direction -= 4
    
        elif d == "L":
            direction -= 1
            if direction <= -1:
                direction += 4
    
    return position

# https://campus.programmers.co.kr/tryouts/175743/challenges?language=python3