from typing import Union

def circular_shift(x: Union[int, float, str], shift: int) -> str:
    s: str = str(x)
    length: int = len(s)
    if shift > length:
        return s[::-1]
    else:
        split_index: int = length - shift
        return s[split_index:] + s[:split_index]