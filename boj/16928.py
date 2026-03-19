# [접근법]
#
#  X = Y 맵을 만들어두고, 움직일수 있는 6개의 주사위를 집어넣고, hook 패턴으로 해당 칸이면 수정된 칸을 리턴,
#  BFS를 이용하면 될 것.
#
# [Feedback]
# - 처음에 getattr(hooks, key, default)이렇게 썼으나, 이건 dict의 key조회방법이 아님
#   - getattr은 객체용
#   - hooks.get(key, default)로 쓰면 더 깔끔
# - visited[1] 도 True로 해주는게 다른 BFS풀떄 더 안전
# 

import sys
from collections import deque

END = 100
visited = [False] * 101
hooks: dict[int, int] = {}


n, m = map(int, sys.stdin.readline().split())

for _ in range(n + m):
    k, v = map(int, sys.stdin.readline().split())
    hooks[k] = v


def solve():
    q = deque([(1, 0)])  # pos, step
    visited[1] = True

    while q:
        pos, step = q.popleft()

        if pos == END:
            return step

        for dice in range(1, 7):
            nxt = pos + dice
            if 100 < nxt:
                continue

            nxt: int = hooks.get(nxt, nxt)

            if not visited[nxt]:
                q.append((nxt, step + 1))
                visited[nxt] = True


print(solve())
