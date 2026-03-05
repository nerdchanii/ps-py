import sys
from functools import reduce

_ = sys.stdin.readline()
numbers = list(map(int, sys.stdin.readline().split(" ")))

result = reduce(lambda x, y: x + ((y + 1) // 2), numbers, 0)
print(result)
