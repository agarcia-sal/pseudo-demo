from typing import Callable


def is_multiply_prime(q: int) -> bool:
    def is_prime(w: int) -> bool:
        if w < 2:
            return False
        for y in range(2, w):
            if w % y == 0:
                return False
        return True

    for h in range(2, 101):
        if not is_prime(h):
            continue
        for u in range(2, 101):
            if not is_prime(u):
                continue
            for o in range(2, 101):
                if not is_prime(o):
                    continue
                if h * u * o == q:
                    return True
    return False