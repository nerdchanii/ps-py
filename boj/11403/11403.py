
from asyncio import sleep
import sys
from collections import deque
n = int(sys.stdin.readline().strip())

graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]



def solve(graph,n):
    mark = [[0] * n for _ in range(n)]
    for start in range(n):
        for end in range(n):
            if mark[start][end] == 1: # 이미 방문처리 된곳이면 이미 조사끝 건너뛰자
                continue
            queue = deque()
            for j in range(n): # A-> B 가능한 노드 다 탐색해서 대기
                if graph[start][j]:
                    queue.append(j)
                    mark[start][j] = 1
            while len(queue):
                curr_node = queue.popleft()
                for to in range(n):
                    if graph[curr_node][to] and mark[start][to] == 0:
                        queue.append(to)
                        mark[start][to] = 1 
                        mark[curr_node][to] = 1
    
    out ='\n'.join(' '.join(str(mark[i][j]) for j in range(n)) for i in range(n))
    print(out)  # noqa: F821

solve(graph, n)