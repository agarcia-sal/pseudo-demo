from typing import Union

def digits(p: Union[int, str]) -> int:
    r: int = 1
    a: int = 0
    i: int = 0
    p_str: str = str(p)
    while i < len(p_str):
        c: str = p_str[i:i + 1]
        d: int = int(c)
        if d % 2 != 0:
            r = r * d
            a += 1
        i += 1
    if a == 0:
        return 0
    return r