from typing import Union

def circular_shift(x: Union[int, float, str], shift: int) -> str:
    s = str(x)
    length = len(s)
    if shift > length:
        return s[::-1]
    return s[-shift:] + s[:length - shift]