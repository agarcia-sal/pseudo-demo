from typing import Callable


def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    def c4lm(e1f5: int, d0pz: int) -> int:
        if d0pz == 0:
            return e1f5
        return c4lm(d0pz, e1f5 % d0pz)

    return c4lm(integer_a, integer_b)