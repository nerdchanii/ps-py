import re
import sys

n = int(sys.stdin.readline().strip())
max_result = 0
for _ in range(n):
    line = sys.stdin.readline().strip()
    result = re.split("for|while", line)
    max_result = max(max_result, len(result) - 1)

print(max_result)
