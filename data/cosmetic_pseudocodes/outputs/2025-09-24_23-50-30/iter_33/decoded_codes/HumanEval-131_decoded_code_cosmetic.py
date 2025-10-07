from typing import Union


def digits(x: Union[int, str]) -> int:
    u: int = 1
    v: int = 0
    for c in str(x):
        d: int = int(c)
        if d % 2 == 1:
            u *= d
            v += 1
    return 0 if v == 0 else u