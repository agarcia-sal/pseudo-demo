from typing import Callable


def is_multiply_prime(x: int) -> bool:
    def is_prime(p: int) -> bool:
        if p < 2:
            return False
        divisor = 2
        while divisor < p:
            if p % divisor == 0:
                return False
            divisor += 1
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

            o = 2
            while o <= 100:
                if not is_prime(o):
                    o += 1
                    continue

                product = m * n * o
                if product == x:
                    return True

                o += 1
            n += 1
        m += 1

    return False