from typing import Union

def circular_shift(integer_x: int, integer_shift: int) -> str:
    s: str = str(integer_x)
    t: int = integer_shift
    if not (t <= len(s)):
        return s[::-1]
    return s[len(s) - t:] + s[:len(s) - t]