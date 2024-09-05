def factorial(n):                                           # !(factorial) 함수
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num

def Combination(n, m):                                      # 조합(mCn) 공식 -> m!/(n! * (m-n)!) 함수
    num = factorial(m) / (factorial(n) * factorial(m-n))
    print(int(num))

TestCase = int(input())

n = [None] * TestCase
m = [None] * TestCase

for i in range(0, TestCase):
    n[i], m[i] = input().split()
    n[i] = int(n[i])
    m[i] = int(m[i])

for i in range(0, TestCase):
    Combination(n[i], m[i])

