from typing import Union

def change_base(x: int, base: int) -> str:
    ret: str = ""
    while x > 0:
        digit: int = x % base
        ret = str(digit) + ret
        x //= base
    return ret