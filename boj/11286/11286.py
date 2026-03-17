import sys
from typing import Generic, TypeVar

T = TypeVar("T")


class ABSMinHeap(Generic[T]):
    """
    절대값이 가장 작은 힙을 구성한다. 힙의 root(peek)는 Abs가 Min인 값을 위로 올려야한다.
    """

    def __init__(self):
        self.__inner__: list[T] = []

    def __shiftdown__(self, idx: int):
        parent = idx
        while parent < self.size:
            target = parent
            left = (parent * 2) + 1
            right = (parent * 2) + 2
            if left < self.size and self.__less__(self[left], self[target]):  # abs
                target = left
            if right < self.size and self.__less__(self[right], self[target]):
                target = right
            if target == parent:
                break
            self[parent], self[target] = self[target], self[parent]
            parent = target

    def __shiftup__(self, idx: int):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.__less__(self[parent], self[idx]):
                break
            self[parent], self[idx] = self[idx], self[parent]
            idx = parent

    def insert(self, x) -> None:
        self.__inner__.append(x)
        self.__shiftup__(self.size - 1)

    def pop(self):
        if self.size == 0:
            return 0
        elif self.size == 1:
            return self.__inner__.pop()
        root = self[0]
        self[0] = self.__inner__.pop()
        self.__shiftdown__(0)
        return root

    @property
    def size(self) -> int:
        return len(self.__inner__)

    def __getitem__(self, k):
        return self.__inner__[k]

    def __setitem__(self, k, value):
        self.__inner__[k] = value

    def __less__(self, left, right):
        return (abs(left), left) < (abs(right), right)


_, *values = sys.stdin.readlines()
values = map(int, values)


def solve(values):
    heap = ABSMinHeap()
    for v in values:
        if v != 0:
            heap.insert(v)
        else:
            print(heap.pop())


solve(values)
