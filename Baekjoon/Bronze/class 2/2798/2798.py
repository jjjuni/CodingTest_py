N, M = map(int, input().split())
result = 0

card = list(map(int, input().split()))
card.sort(reverse=True)

for i in range(N - 2):
    for j in range(i+1, N - 1):
        for k in range(j+1, N):
            if card[i] + card[j] + card[k] <= M and card[i] + card[j] + card[k] > result:
                result = card[i] + card[j] + card[k]
            if result == M:
                break
        if result == M:
            break
    if result == M:
        break

print(result)