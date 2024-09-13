import sys

def compare(a, b, c, d):                # 시간표 비교 함수 (안겹치면 True, 겹치면 False 반환)

    if a >= d or c >= b:
        return True
    else:
        return False

N = int(sys.stdin.readline())

inf = [[] for _ in range(N)]

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())

    inf[i].append(a)
    inf[i].append(b)

inf.sort(key=lambda x: (x[0], x[1]))

i = 0
while i < len(inf) - 1:
    j = i + 1
    while j < len(inf):
        if compare(inf[i][0], inf[i][1], inf[j][0], inf[j][1]):
            inf[i][1] = inf[j][1]
            inf.pop(j)

        else:
            j += 1

    i += 1

print(len(inf))

# 참고자료 (sort(key))
# https://rnrmffj.tamchart.com/74
# https://gusugi.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-sorted-%ED%95%A8%EC%88%98-%EC%9D%B4%ED%95%B4-%EB%B0%8F-%ED%99%9C%EC%9A%A9%EB%B2%95-key-%EB%A7%A4%EA%B0%9C%EB%B3%80%EC%88%98-%ED%99%9C%EC%9A%A9%EB%B2%95