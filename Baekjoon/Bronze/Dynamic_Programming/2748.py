def fibo(num, a, b):
    if num > 0:
        return fibo(num - 1, b, a + b)
    else:
        return a + b
    
num = int(input())
a = 0
b = 1

if num == 0:
    print(0)

elif num == 1:
    print(1)

else:
    num -= 2
    print(fibo(num, a, b))