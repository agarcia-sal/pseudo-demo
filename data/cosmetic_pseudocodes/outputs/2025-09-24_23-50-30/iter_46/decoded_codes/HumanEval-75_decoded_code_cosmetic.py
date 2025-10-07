from typing import Callable


def is_multiply_prime(xq: int) -> bool:
    def is_prime(xz: int) -> bool:
        def prime_check(yv: int) -> bool:
            if yv >= xz:
                return True
            if xz % yv != 0:
                return prime_check(yv + 1)
            return False
        return prime_check(2)

    def outer_loop(mn: int) -> bool:
        if mn > 100:
            return False
        if not is_prime(mn):
            return outer_loop(mn + 1)
        return middle_loop(2, mn)

    def middle_loop(pb: int, aq: int) -> bool:
        if pb > 100:
            return outer_loop(aq + 1)
        if not is_prime(pb):
            return middle_loop(pb + 1, aq)
        return inner_loop(2, aq, pb)

    def inner_loop(hm: int, er: int, dq: int) -> bool:
        if hm > 100:
            return middle_loop(er + 1, dq)
        if not is_prime(hm):
            return inner_loop(hm + 1, er, dq)
        if dq * er * hm == xq:
            return True
        return inner_loop(hm + 1, er, dq)

    return outer_loop(2)