from typing import Union


def circular_shift(integer_x: int, integer_shift: int) -> str:
    s: str = str(integer_x)
    length: int = len(s)
    if integer_shift > length:
        return "".join(reversed(s))
    else:
        return s[length - integer_shift : length] + s[0 : length - integer_shift]