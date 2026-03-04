import sys

n, m = map(int, sys.stdin.readline().split())

n *= 100

print("Yes" if n >= m else "No")
