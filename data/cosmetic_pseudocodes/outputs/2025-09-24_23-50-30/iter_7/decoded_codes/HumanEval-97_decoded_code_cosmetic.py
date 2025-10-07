from typing import Callable

def multiply(x1: int, x2: int) -> int:
    def mod_abs(val: int) -> int:
        if val < 0:
            val = -val
        return val - ((val // 10) * 10)

    y1: int = mod_abs(x1)
    y2: int = mod_abs(x2)

    result: int = 0
    count: int = y2

    while count > 0:
        result += y1
        count -= 1

    return result