import sys
from collections import deque
from copy import deepcopy
from multiprocessing.connection import answer_challenge

n, m = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

answer = 0

max_len = 4
max_value = max(map(max, board))

DIRS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
visited = [[False] * m for _ in range(n)]


def dfs(x, y, depth, score):
    global answer

    if score + ((max_len - depth) * max_value) <= answer:
        return

    if depth == 4:
        answer = max(answer, score)
        if answer == score:
            print(visited)
        return
    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue  # Out of board
        if visited[nx][ny]:
            continue

        if depth == 2:
            visited[nx][ny] = True
            dfs(x, y, depth + 1, score + board[nx][ny])
            visited[nx][ny] = False

        visited[nx][ny] = True
        dfs(nx, ny, depth + 1, score + board[nx][ny])
        visited[nx][ny] = False


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False


print(answer)
