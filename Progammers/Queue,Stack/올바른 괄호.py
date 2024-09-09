def solution(s):
    s = list(s)
    stack = []

    for i in range(len(s)):

        if s[i] == '(':             # '('로 괄호를 열었을 시 
            stack.append('0')       # 스택에 push

        elif s[i] == ')':           # ')'로 괄호를 닫았을 시
            if len(stack) <= 0:          # '('보다 ')'가 먼저 나올 경우 flag는 -1이 됨 
                return False            # -> 이 경우 즉시 종료 후 false
            else:                   
                stack.pop()         # 스택에서 pop

    if len(stack) == 0:
        return True
    else:
        return False
    
print(solution("()()(("))