from collections import deque

def solution(maps):
    queue = deque([])

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    n = len(maps)      # 행
    m = len(maps[0])   # 열

    queue.append([0, 0, 1])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True

    while queue:
        x, y, count = queue.popleft()

        if x == m - 1 and y == n - 1:
            return count

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and maps[ny][nx] == 1:
                    visited[ny][nx] = True
                    queue.append([nx, ny, count + 1])

    return -1

# https://campus.programmers.co.kr/tryouts/175956/challenges?language=python3