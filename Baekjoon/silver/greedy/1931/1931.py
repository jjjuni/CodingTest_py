import sys

N = int(sys.stdin.readline())

timetable = []                  # [[회의 시작 시간, 회의 종료 시간], ...]

result = []                     # [회의 종료 시간, 겹치지 않는 다음 회의 종료 시간, ...]

for i in range(N):
    timetable.append(list(map(int, sys.stdin.readline().split())))

timetable.sort(key=lambda x: (x[1], x[0]))            # 종료 시간 오름차순 정렬 (종료 시간이 같다면 시작 시간 오름차순 정렬)

result.append(timetable[0][1])

for i in range(1, N):
    if result[-1] <= timetable[i][0]:
        result.append(timetable[i][1])
    
print(len(result))

