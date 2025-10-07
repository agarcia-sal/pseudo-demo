from typing import Union

def digits(n: Union[int, str]) -> int:
    p: int = 1
    c: int = 0
    s: list[str] = list(str(n))
    i: int = 0

    while i < len(s):
        x: int = int(s[i])
        if x % 2 != 0:
            p *= x
            c += 1
        i += 1

    return p if c > 0 else 0