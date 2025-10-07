from typing import Union

def change_base(x: int, base: int) -> str:
    ret: str = ''
    if x == 0:
        return '0'
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret