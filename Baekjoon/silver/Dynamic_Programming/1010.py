def Bridge(n, m):
    num = 1

    for i in range (0, n):
        num *= (m-(n-(i+1)))

    print(num)

TestCase = int(input())

n = [None] * TestCase
m = [None] * TestCase

for i in range(0, TestCase):
    n[i] = int(input())
    m[i] = int(input())
    
print("\n")

for i in range(0, TestCase):
    Bridge(n[i], m[i])

