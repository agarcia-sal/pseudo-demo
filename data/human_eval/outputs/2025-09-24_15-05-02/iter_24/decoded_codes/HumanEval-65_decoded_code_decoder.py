from typing import Union

def circular_shift(x: Union[int, str], shift: int) -> str:
    s: str = str(x)
    length: int = len(s)
    if shift > length:
        return s[::-1]
    return s[-shift:] + s[:length - shift]