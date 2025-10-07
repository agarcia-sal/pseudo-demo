from typing import Callable


def is_multiply_prime(g: int) -> bool:
    def is_prime(h: int) -> bool:
        if h < 2:
            return False
        for v in range(2, h):
            if h % v == 0:
                return False
        return True

    for m in range(2, 101):
        if not is_prime(m):
            continue
        for n in range(2, 101):
            if not is_prime(n):
                continue
            for o in range(2, 101):
                if not is_prime(o):
                    continue
                r = m * n * o
                if r == g:
                    return True
    return False