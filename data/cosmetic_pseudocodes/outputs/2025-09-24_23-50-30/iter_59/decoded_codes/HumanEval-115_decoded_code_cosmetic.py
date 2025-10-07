from math import ceil
from typing import List


def max_fill(a1: List[int], a2: int) -> int:
    def a3(a4: int) -> int:
        return 0 if a4 == 0 else a4

    def a5(a6: List[int]) -> int:
        if not a6:
            return 0
        return a6[0] + a5(a6[1:])

    def a7(a8: List[int]) -> int:
        return a3(ceil(a5(a8) / a2))

    def a9(a10: int, a11: int, a12: int) -> int:
        if a10 == a11:
            return a12
        return a9(a10 + 1, a11, a12 + a7(a1[a10]))

    return a9(0, len(a1), 0)