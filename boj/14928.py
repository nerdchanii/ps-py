import sys

big_number = sys.stdin.readline().strip()
divisor = 20_000_303

remain = 0
value = 0
for cur in big_number:
    remain = (remain * 10) + int(cur)
    remain = remain % divisor
print(remain)
