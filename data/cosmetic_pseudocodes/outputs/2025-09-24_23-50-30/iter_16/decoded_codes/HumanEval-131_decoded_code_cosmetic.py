from typing import Tuple


def digits(n: int) -> int:
    nums = [int(c) for c in str(n)]

    def rec(i: int, p: int, c: int) -> Tuple[int, int]:
        if i == len(nums):
            return p, c
        d = nums[i]
        if d % 2 != 0:
            return rec(i + 1, p * d, c + 1)
        else:
            return rec(i + 1, p, c)

    p, c = rec(0, 1, 0)
    if c == 0:
        return 0
    return p