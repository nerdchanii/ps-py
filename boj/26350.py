import sys

tc_amount = int(sys.stdin.readline())
outs = []
for _ in range(tc_amount):
    _, *denominations = list(map(int, sys.stdin.readline().split(" ")))
    good_state = True
    for i in range(0, len(denominations) - 1):
        next = i + 1
        if denominations[i] * 2 > denominations[next]:
            good_state = False
            break
    outs.append(f"""Denominations: {" ".join(map(str, denominations))}
{"Good" if good_state else "Bad"} coin denominations!""")

print("\n\n".join(outs))
