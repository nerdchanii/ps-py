# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    그림.py                                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yechakim <yechakim@student.42seoul.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 1926/01/01 00:00:00 by                   #+#    #+#              #
#    Updated: 2025/07/17 20:05:00 by yechakim         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

visited = [[False] * m for _ in range(n)]


def dfs(x, y):
    stack = [(x, y)]
    if graph[x][y] == 0 or visited[x][y]:
        return 0
    visited[x][y] = True
    size = 1
    while len(stack) > 0:
        x, y = stack.pop()
        for dx, dy in d:
            ny = y + dy
            nx = x + dx
            if (
                0 <= nx < n
                and 0 <= ny < m
                and not visited[nx][ny]
                and graph[nx][ny] == 1
            ):
                stack.append((nx, ny))
                size += 1
    return size


max_size = 0
cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            size = dfs(i, j)
            max_size = max(max_size, size)

print(cnt)
print(max_size)
