from typing import Callable


def circular_shift(integer_x: int, integer_shift: int) -> str:
    s: str = str(integer_x)
    length: int = len(s)

    def shift_func(n: int, k: int) -> str:
        if not (0 <= k <= n):
            # If k is out of bounds, return reversed string
            return s[::-1]
        else:
            # Return circularly shifted string
            return s[n - k : n] + s[0 : n - k]

    return shift_func(length, integer_shift)