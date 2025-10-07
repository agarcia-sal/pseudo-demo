from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for x in range(2, num):
            if num % x == 0:
                return False
        return True

    for iterator_i in range(2, 101):
        if not is_prime(iterator_i):
            continue
        for iterator_j in range(2, 101):
            if not is_prime(iterator_j):
                continue
            for iterator_k in range(2, 101):
                if not is_prime(iterator_k):
                    continue
                product = iterator_i * iterator_j * iterator_k
                if product == a:
                    return True
    return False