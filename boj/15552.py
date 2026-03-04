import sys

it = iter(sys.stdin)
_ = next(it)

for line in it:
    a, b = map(int, line.split())
    print(a + b)
