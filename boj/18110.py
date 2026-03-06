import math
import sys

n, *nums = map(int, sys.stdin.readlines())
if n == 0:
    print(0)
    exit()
nums.sort(reverse=True)

fifteen = math.floor((n * 0.15) + 0.5)

sums = sum(nums[fifteen : n - fifteen])
resized_n = n - 2 * fifteen
result = math.floor((sums / resized_n) + 0.5)

print(result)
