from typing import NoReturn


def is_multiply_prime(q: int) -> bool:
    def is_prime(h: int) -> bool:
        if h < 2:
            return False
        w = 2
        while w * w <= h:
            if h % w == 0:
                return False
            w += 1
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
                if m * n * o == q:
                    return True
    return False