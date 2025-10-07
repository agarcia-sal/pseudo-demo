from typing import List


def add(lst: List[int]) -> int:
    return sum(x for i, x in enumerate(lst, start=1) if i % 2 == 1 and x % 2 == 0)