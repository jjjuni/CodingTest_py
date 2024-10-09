import sys
sys.setrecursionlimit(10**6)


N, K = map(int, (input().split()))

coin_dictionary = {}
coin_list = []

for i in range(N):
    num = int(input())
    coin_dictionary[num] = 0
    coin_list.append(num)

coin_dictionary[K] = 0
coin_list.sort()
