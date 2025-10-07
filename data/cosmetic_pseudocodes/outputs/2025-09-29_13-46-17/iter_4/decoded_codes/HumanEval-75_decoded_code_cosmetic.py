from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        def check_divisor(x: int) -> bool:
            if x >= n:
                return True
            if n % x != 0:
                return check_divisor(x + 1)
            return False
        return check_divisor(2)

    index_i: int = 2
    while index_i <= 100:
        if is_prime(index_i):
            index_j: int = 2
            while index_j <= 100:
                if is_prime(index_j):
                    index_k: int = 2
                    while True:
                        if index_k > 100:
                            break
                        if not is_prime(index_k):
                            index_k += 1
                            continue
                        if index_i * index_j * index_k == a:
                            return True
                        index_k += 1
                index_j += 1
        index_i += 1
    return False