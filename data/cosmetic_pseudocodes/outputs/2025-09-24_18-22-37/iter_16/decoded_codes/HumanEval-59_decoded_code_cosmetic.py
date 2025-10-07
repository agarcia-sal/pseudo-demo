from typing import Callable


def largest_prime_factor(xq: int) -> int:
    def is_prime(ae: int) -> bool:
        if ae < 2:
            return False
        f3 = 2
        while f3 < ae:
            if ae % f3 == 0:
                return False
            f3 += 1
        return True

    lk = 1
    qh = 2
    while qh <= xq:
        if xq % qh == 0:
            if is_prime(qh):
                lk = lk if lk > qh else qh
        qh += 1
    return lk