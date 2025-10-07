from typing import Literal


def is_multiply_prime(op: int) -> bool:
    def is_prime(val: int) -> bool:
        if val < 2:
            return False
        x = 2
        while x <= val - 1:
            if val % x == 0:
                return False
            x += 1
        return True

    m = 2
    while m <= 100:
        if not is_prime(m):
            m += 1
            continue
        n = 2
        while n <= 100:
            if not is_prime(n):
                n += 1
                continue
            p = 2
            while True:
                if not is_prime(p):
                    p += 1
                    next_loop = True
                else:
                    product = m * n * p
                    if product == op:
                        return True
                    else:
                        p += 1
                        next_loop = False
                if p > 100 or next_loop:
                    break
            if next_loop:
                continue
            n += 1
        m += 1

    return False