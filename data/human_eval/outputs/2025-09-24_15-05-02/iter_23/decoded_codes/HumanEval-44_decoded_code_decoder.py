from typing import Union

def change_base(x: int, base: int) -> str:
    if base <= 1:
        raise ValueError("base must be greater than 1")
    if x == 0:
        return "0"
    ret: str = ""
    abs_x = abs(x)
    while abs_x > 0:
        ret = str(abs_x % base) + ret
        abs_x //= base
    return ret if x >= 0 else "-" + ret