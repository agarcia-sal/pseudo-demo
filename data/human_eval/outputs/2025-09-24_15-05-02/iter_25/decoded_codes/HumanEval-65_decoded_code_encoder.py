from typing import Union

def circular_shift(integer_x: int, integer_shift: int) -> str:
    s: str = str(integer_x)
    length: int = len(s)
    if integer_shift > length:
        return s[::-1]
    else:
        split_point: int = length - integer_shift
        return s[split_point:] + s[:split_point]