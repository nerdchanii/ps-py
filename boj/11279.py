"""
problem: max heap
"""

import sys

DEL = 0


class Maxheap:
    def __init__(self):
        self._inner = []

    def __shiftdown__(self, parent):
        n = self.size
        while True:
            target = parent
            left = (parent * 2) + 1
            right = (parent * 2) + 2

            if left < n and self._inner[target] < self._inner[left]:
                target = left
            if right < n and self._inner[target] < self._inner[right]:
                target = right

            if target == parent:
                break

            self._inner[parent], self._inner[target] = (
                self._inner[target],
                self._inner[parent],
            )
            parent = target

    def __shiftup__(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2  # [0. 1, 2, 3,4, 5,6]
            if self._inner[idx] <= self._inner[parent]:
                break
            self._inner[parent], self._inner[idx] = (
                self._inner[idx],
                self._inner[parent],
            )
            idx = parent

    def pop(self):
        if self.size == 0:
            return 0
        x = self.root
        lastitem = self._inner.pop()
        if self.size == 0:
            return lastitem
        self._inner[0] = lastitem
        self.__shiftdown__(0)
        return x

    def insert(self, x):
        self._inner.append(x)
        self.__shiftup__(self.size - 1)

    @property
    def root(self):
        return self._inner[0]

    @property
    def size(self):
        return len(self._inner)


h = Maxheap()

it = iter(map(int, sys.stdin))
_n = next(it)
for item in it:
    if item == DEL:
        print(h.pop())
    else:
        h.insert(item)
