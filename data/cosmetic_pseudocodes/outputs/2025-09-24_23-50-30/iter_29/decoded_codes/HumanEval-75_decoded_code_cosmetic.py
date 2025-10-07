from typing import Callable


def is_multiply_prime(x: int) -> bool:
    def is_prime(m: int) -> bool:
        def check_divisor(d: int) -> bool:
            if d >= m:
                return True
            if m % d == 0:
                return False
            return check_divisor(d + 1)
        return check_divisor(2)

    index_a = 2
    while index_a <= 100:
        if is_prime(index_a):
            index_b = 2
            while index_b <= 100:
                if is_prime(index_b):
                    index_c = 2
                    while index_c <= 100:
                        if is_prime(index_c):
                            if (index_a * index_b) * index_c == x:
                                return True
                        index_c += 1
                index_b += 1
        index_a += 1
    return False