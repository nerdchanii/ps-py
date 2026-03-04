import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2


class Turret:
    def __init__(self, x, y, r):
        self._pos = Point(x, y)
        self.r = r

    def get_distance(self, other):
        return self._pos.get_distance(other._pos)


def solve(a, b):
    distance = a.get_distance(b)
    if distance == 0:
        return -1 if r1 == r2 else 0

    sum_r = a.r + b.r
    diff_r = abs(a.r - b.r)

    sum2 = sum_r * sum_r
    diff2 = diff_r * diff_r
    if distance == sum2 or distance == diff2:
        return 1  # 내,외접
    elif diff2 < distance < sum2:
        return 2
    else:
        return 0


n = int(sys.stdin.readline())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(float, sys.stdin.readline().split(" "))
    t1 = Turret(x1, y1, r1)
    t2 = Turret(x2, y2, r2)
    answer = solve(t1, t2)
    print(answer)
