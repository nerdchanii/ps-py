# 접근법
#
#  X = Y 맵을 만들어두고, 움직일수 있는 6개의 주사위를 집어넣고, hook 패턴으로 해당 칸이면 수정된 칸을 리턴,
#  BFS를 이용하면 될 것.
#


import sys
from collections import deque

dices = [1, 2, 3, 4, 5, 6]
visited = [False] * 101
hooks = {}
END = 100


n, m = map(int, sys.stdin.readline().split(" "))

for _ in range(n + m):
    k, v = map(int, sys.stdin.readline().split(" "))
    hooks[k] = v


def solve(dices, hooks):
    q = deque()  # pos, step
    q.append((1, 0))
    while len(q):
        pos, step = q.popleft()
        if pos == END:
            return step
        for dice in dices:
            next = pos + dice
            if next in hooks:
                next = hooks[next]
            if next <= 100 and not visited[next]:
                q.append((next, step + 1))
                visited[next] = True


print(solve(dices, hooks))
