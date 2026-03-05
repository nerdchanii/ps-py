import sys

people, recommended_distance = map(int, sys.stdin.readlines())

print((people - 1) * recommended_distance)
