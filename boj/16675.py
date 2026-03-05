import sys
from typing import Set

ml, mr, tl, tr = sys.stdin.readline().strip().split(" ")

WIN_RSP = {
    "R": "S",
    "S": "P",
    "P": "R",
}


def solve(ms: Set, tk: Set):
    if len(ms) == 2 and len(tk) == 2:
        return "?"
    elif len(ms) == 1 and len(tk) == 1:
        ms_choice = ms.pop()
        tk_choice = tk.pop()
        result = "?"
        if WIN_RSP[ms_choice] == tk_choice:
            result = "MS"
        elif WIN_RSP[tk_choice] == ms_choice:
            result = "TK"
        return result
    elif len(ms) == 1:
        tk_win = False
        ms_value = ms.pop()
        for t in tk:
            if WIN_RSP[t] == ms_value:
                tk_win = True
        return "TK" if tk_win else "?"
    else:
        ms_win = False
        value = tk.pop()
        for m in ms:
            if WIN_RSP[m] == value:
                ms_win = True
        return "MS" if ms_win else "?"


answer = solve(set([ml, mr]), set([tl, tr]))
print(answer)
