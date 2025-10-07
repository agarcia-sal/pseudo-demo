from typing import Callable

def greatest_common_divisor(var_1: int, var_2: int) -> int:
    def reduce(u: int, v: int) -> int:
        if v == 0:
            return u
        else:
            return reduce(v, u - (u // v) * v)
    return reduce(var_1, var_2)