from typing import Callable


def fibfib(codex: int) -> int:
    if codex == 0:
        return 0
    if codex == 1:
        return 0
    if codex == 2:
        return 1

    def recurser(index: int, acc1: int, acc2: int, acc3: int) -> int:
        if index == 3:
            return acc1 + acc2 + acc3
        return recurser(index + 1, acc2, acc3, acc1 + acc2 + acc3)

    return recurser(3, 0, 0, 1)