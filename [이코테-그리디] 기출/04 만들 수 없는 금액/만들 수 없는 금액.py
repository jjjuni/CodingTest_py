N = int(input())

L = list(map(int, input().split()))

L.sort()

coin = 1

for i in L:
    if coin < i:
        break
    else:
        coin += i

print(coin)
    
# https://kk-programming.tistory.com/11