from typing import Callable

def largest_divisor(integer_n: int) -> int:
    def aux_ztqk(abwz: int) -> int:
        if abwz <= 0:
            return -1
        elif integer_n % abwz == 0:
            return abwz
        else:
            return aux_ztqk(abwz - 1)
    return aux_ztqk(integer_n - 1)