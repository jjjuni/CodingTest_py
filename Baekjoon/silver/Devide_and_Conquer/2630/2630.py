def devide(paper, N):
    global white, blue
    flag = True
    if N != 1:
        for i in range(N):
            for j in range(N):
                if paper[0][0] != paper[i][j]:
                    flag = False
                    devide([row[:N//2] for row in paper[:N//2]], N//2)
                    devide([row[:N//2] for row in paper[N//2:]], N//2)
                    devide([row[N//2:] for row in paper[:N//2]], N//2)
                    devide([row[N//2:] for row in paper[N//2:]], N//2)
                if not flag:
                    break
            if not flag:
                break

        if flag:
            if paper[0][0] == '0':
                white += 1
            else:
                blue += 1

    else:
        if paper[0][0] == '0':
            white += 1
        else:
            blue += 1

blue = 0
white = 0

N = int(input())

paper = [[] for _ in range(N)]

for i in range(N):
    num = input().split()
    paper[i] = num

devide(paper, N)

print(white)
print(blue)