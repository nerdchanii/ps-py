import sys

CORRET = "correct!"
WRONG = "wrong!"


a, b, c = map(int, sys.stdin.readline().split(" "))

if (a + b) == c:
    print(CORRET)
else:
    print(WRONG)
