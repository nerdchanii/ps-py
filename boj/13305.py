import sys
from typing import Dict, Generic, Optional, TypeVar

TC_AMOUNT = int(sys.stdin.readline().strip())
DEL_MAX = "D 1"
DEL_MIN = "D -1"

T = TypeVar("T", int, float)


class Heap(Generic[T]):
    def __init__(self, min=True):
        self._inner: list[T] = []
        self._is_min = min

    def push(self, value: T) -> None:
        self._inner.append(value)
        self.__shift_up__(len(self._inner) - 1)

    def pop(self) -> Optional[T]:
        n = len(self._inner)
        if n == 0:
            return None
        if n == 1:
            return self._inner.pop()
        top = self._inner[0]
        self._inner[0] = self._inner.pop()
        self.__shift_down__(0)
        return top

    def peek(self) -> Optional[T]:
        return self._inner[0] if self._inner else None

    def __shift_up__(self, index: int) -> None:
        while index > 0:
            parent = (index - 1) // 2
            if self.__prior__(index, parent):
                self.__swap__(index, parent)
                index = parent
            else:
                break

    def __shift_down__(self, idx: int):
        n = len(self._inner)
        while True:
            left = (idx * 2) + 1
            if left >= n:
                break
            right = left + 1
            target = left

            if right < n and self.__prior__(right, left):
                target = right
            if self.__prior__(target, idx):
                self.__swap__(target, idx)
                idx = target
            else:
                break

    def __swap__(self, a_idx, b_idx):
        self._inner[a_idx], self._inner[b_idx] = self._inner[b_idx], self._inner[a_idx]

    def __prior__(self, a_idx, b_idx) -> bool:
        a = self._inner[a_idx]
        b = self._inner[b_idx]
        return a < b if self._is_min else a > b


class DEPQ(Generic[T]):
    def __init__(self) -> None:
        self.minh = Heap(min=True)
        self.maxh = Heap(min=False)
        self.counts: Dict[T, int] = {}
        self.n = 0

    def insert(self, value):
        self.minh.push(value)
        self.maxh.push(value)
        self.counts[value] = self.counts.get(value, 0) + 1
        self.n += 1

    def prune_min(self):
        while True:
            peek = self.minh.peek()
            if peek is None:
                return
            if self.counts.get(peek, 0) == 0:
                self.minh.pop()
                continue
            break

    def prune_max(self):
        while True:
            peek = self.maxh.peek()
            if peek is None:
                return
            if self.counts.get(peek, 0) == 0:
                self.maxh.pop()
                continue
            break

    def deleteMin(self) -> Optional[T]:
        if self.n == 0:
            return None
        self.prune_min()
        x = self.minh.pop()
        self.n -= 1
        self.counts[x] -= 1
        if self.counts[x] == 0:
            del self.counts[x]
        return x

    def deleteMax(self) -> Optional[T]:
        if self.n == 0:
            return None
        self.prune_max()
        x = self.maxh.pop()
        self.n -= 1
        self.counts[x] -= 1
        if self.counts[x] == 0:
            del self.counts[x]
        return x

    def findMin(self):
        if self.n == 0:
            return None
        self.prune_min()
        return self.minh.peek()

    def findMax(self):
        if self.n == 0:
            return None
        self.prune_max()
        return self.maxh.peek()

    def __len__(self):
        return self.n


def solve(opers: list[str]):
    q = DEPQ()
    for line in opers:
        if line in [DEL_MAX, DEL_MIN]:
            if len(q) == 0:
                continue
            if line == DEL_MAX:
                q.deleteMax()
            else:
                q.deleteMin()
        else:
            _, N = line.split(" ")
            N = int(N)
            q.insert(N)
    return q


for _ in range(TC_AMOUNT):
    opers_amount = int(sys.stdin.readline().strip())
    cases = [sys.stdin.readline().strip() for _ in range(opers_amount)]
    q = solve(cases)
    if len(q) == 0:
        print("EMPTY")
    else:
        print(f"{q.findMax()} {q.findMin()}")
