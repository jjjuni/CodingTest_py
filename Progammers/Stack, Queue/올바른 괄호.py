flag = 0
index = 0

def solution(T, flag, index):
    if flag < 0:                # '('보다 ')'가 먼저 나올 경우 flag는 -1이 됨 -> 이 경우 즉시 종료 후 false 반환
        return
    
    elif T[index] == '(':       # '('로 괄호를 열었을 시 flag++ 
        flag += 1

    elif T[index] == ')':       # ')'로 괄호를 닫았을 시 flag--
        flag -= 1

    index += 1

    if index >= len(T):
        solution(T, flag, index)

    return flag

T = input()

T = list(T)

flag = solution(T, flag, index)

print(flag)

if flag == 0:
    print("true")
else:
    print("false")