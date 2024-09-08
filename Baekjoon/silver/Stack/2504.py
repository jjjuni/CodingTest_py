Stack = []

result = 0
index = 0

s = input()

def solution():
    global index
    result = 0
    if len(s) - 1 <= index:
        return 0
    
    if s[index] == '(':
        Stack.append(2)
        index += 1
        try:
            while s[index] != ')':
                tmp = solution()
                if tmp != 0:
                    result += tmp
                else:
                    return 0
        except IndexError:
            return 0

    elif s[index] == '[':
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

    if s[index] == ')':
        try:
            num = Stack.pop()
        except IndexError:
            return 0
        if num != 2:
            return 0
        if s[index-1] == '(':
            result += num
        else:
            result *= num
        index += 1
        return result
    
    elif s[index] == ']':
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
    
    if len(Stack) == 0 and len(s) > index:
        result += solution()

    elif len(Stack) > 0:
        return 0
    else:
        return result
    
while len(s) > index:
    tmp = solution()
    if tmp != 0:
        result += tmp
    else:
        result = 0
        break

print(result)




# for i in range(len(s)):

#     if (s[i] == ')' or s[i] == ']') and len(Stack) <= 0:
#         print("0")
#         break

#     if s[i] == '(':
#         Stack.append(2)
        
#     elif s[i] == '[':
#         Stack.append(3)
        
#     elif s[i] == ')':
#         if len(Stack) > 1 and result != 0:
#             result *= 2
#         else:
#             result += 2
    



