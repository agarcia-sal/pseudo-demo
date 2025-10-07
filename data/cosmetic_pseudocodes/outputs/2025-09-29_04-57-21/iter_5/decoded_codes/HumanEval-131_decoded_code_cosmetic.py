from typing import Callable

def digits(n: int) -> int:
    acc: int = 1
    tally: int = 0
    chars: str = str(n)

    def recur(idx: int) -> int:
        nonlocal acc, tally
        if idx >= len(chars):
            return acc if tally != 0 else 0
        val: int = int(chars[idx])
        if val % 2 != 0:
            acc *= val
            tally += 1
        return recur(idx + 1)

    return recur(0)