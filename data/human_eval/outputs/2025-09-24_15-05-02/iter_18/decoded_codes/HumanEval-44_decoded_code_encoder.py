from typing import Union

def change_base(x: int, base: int) -> str:
    if x == 0:
        return "0"
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x = x // base
    return ret