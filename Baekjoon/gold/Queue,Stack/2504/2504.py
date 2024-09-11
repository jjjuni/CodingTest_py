Stack = [] 

result = 0                          # 계산 결과값을 저장 할 변수
index = 0                           # 현재 읽고 있는 (문자열의 인덱스)를 나타내는 변수

s = input()                         # 괄호열을 나타내는 문자열 입력 [1 <= (문자열 길이) <= 30]

def solution():                     # 답을 구하는 함수(재귀로 동작)
    global index                        # 전역변수 index 가져옴
    result = 0                          # 전역변수 result와 다른 지역변수 선언

    if len(s) - 1 <= index:             # index가 문자열의 길이를 넘어간다면
        return 0                            # 0을 반환
    
    if s[index] == '(':                 # '(' 로 괄호를 열었다면
        Stack.append(2)                     # Stack 에 2 push
        index += 1                          # index 1 증가
        try:                            
            while s[index] != ')':          # ')' 로 괄호를 닫을 때 까지:
                tmp = solution()                # 재귀 호출 후 값 저장
                if tmp != 0:                    # 재귀 후 얻은 값이 0이 아니라면
                    result += tmp                   # result에 값 저장
                else:                           # 재귀 후 얻은 값이 0이라면 (=오류가 나거나 옳지 않은 괄호열이라면)
                    return 0                        # 0을 return (0을 return 할 시 모든 상위 재귀함수도 0을 return)
                                                    # -> 즉 하나의 오류, 또는 옳지 않은 괄호열이 나오면 모든 재귀함수 return 0 실행

        except IndexError:              # IndexError 예외처리 (')'로 닫지 않을 시 재귀가 계속 진행되기 때문에 예외 처리 필요)
            return 0                        # 0을 반환

    elif s[index] == '[':               # 위 '(' 일 때 와 같은 로직
        Stack.append(3)                 
        index += 1                      
        try:
            while s[index] != ']':
                tmp = solution()
                if tmp != 0:
                    result += tmp
                else:
                    return 0
        except IndexError:
            return 0

    if s[index] == ')':                 # ')' 로 괄호를 닫았다면
        try:                            
            num = Stack.pop()               # Stack 에서 pop() 하여 num에 저장
        except IndexError:                  # 빈 Stack 에서 pop() 을 진행한다면 ('(' 로 열지 않고 ')' 로 닫으려 할 시)
            return 0                            # 0을 반환
        
        if num != 2:                        # '()' 는 값이 2 이므로 pop() 한 값이 2가 아니라면 괄호의 짝이 맞지 않은 것 -> 옳지 않은 괄호열
            return 0                            # 0을 반환
        
        if s[index-1] == '(':               # 바로 이전 문자가 '(' 라면 (현재 괄호열 안에 다른 괄호열이 없기 때문에 더해야 함)
            result += num                       # result 에 num 더하기
        else:                               # 바로 이전 문자가 다른 문자라면 (현재 괄호열이 다른 괄호열을 묶고 있기 때문에 곱해야 함)
            result *= num                       # result 에 num 곱하기
        index += 1                          # index 1 증가 후 result 반환
        return result
    
    elif s[index] == ']':               # 위 ')' 일 때와 같은 로직
        try:
            num = Stack.pop()
        except IndexError:
            return 0
        
        if num != 3:
            return 0
        
        if s[index-1] == '[':
            result += num
        else:
            result *= num
        index += 1
        return result

    else:
        return 0

while len(s) > index:               # 문자열의 끝까지 읽을 때 까지
    tmp = solution()                    # solution 함수 호출
    if tmp != 0:                        # 계산 결과값이 0이 아니라면 (오류 없이 solution 함수 계산이 끝났다면)
        result += tmp                       # 반환값을 result 에 더함
    else:                               # 계산 결과값이 0이라면 (오류가 났다면)
        result = 0                          # result 에 0을 대입, while문 탈출
        break

print(result)