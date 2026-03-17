import sys
from collections import deque

tc_len = sys.stdin.readline()


def get_path(current: int, parent: list[int], how: list[str]) -> list[str]:
    path: list[str] = []
    while how[current] != "":
        path.append(how[current])
        current = parent[current]
    return path[::-1]


def solve(f: int, t: int):
    q = deque()
    visited = [False] * 10000
    parent = [0] * 10000
    how: list[str] = [""] * 10000
    q.append(f)
    visited[f] = True
    while q:
        current = q.popleft()
        d_v = current * 2 % 10000
        s_v = current - 1 if current != 0 else 9999
        l_v = (current % 1000) * 10 + (current // 1000)
        r_v = current // 10 + (current % 10) * 1000

        if not visited[d_v]:
            q.append(d_v)
            visited[d_v] = True
            parent[d_v] = current
            how[d_v] = "D"
            if d_v == t:
                return get_path(d_v, parent, how)
        if not visited[s_v]:
            q.append(s_v)
            visited[s_v] = True
            parent[s_v] = current
            how[s_v] = "S"
            if s_v == t:
                return get_path(s_v, parent, how)
        if not visited[l_v]:
            q.append(l_v)
            visited[l_v] = True
            parent[l_v] = current
            how[l_v] = "L"
            if l_v == t:
                return get_path(l_v, parent, how)
        if not visited[r_v]:
            q.append(r_v)
            visited[r_v] = True
            parent[r_v] = current
            how[r_v] = "R"
            if r_v == t:
                return get_path(r_v, parent, how)
    return ["-1"]


for _ in range(int(tc_len)):
    f, t = map(int, sys.stdin.readline().split())
    result: list[str] = solve(f, t)
    print("".join(result))
