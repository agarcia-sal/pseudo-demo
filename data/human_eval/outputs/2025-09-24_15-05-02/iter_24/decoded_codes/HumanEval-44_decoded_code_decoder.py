from typing import Union

def change_base(x: int, base: int) -> str:
    if x == 0:
        return "0"
    if base <= 1:
        raise ValueError("Base must be greater than 1")

    ret: str = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret