from typing import Iterator


def is_prime(integer_n: int) -> bool:
    if integer_n < 2:
        return False
    for integer_k in range(2, integer_n):
        if integer_n % integer_k == 0:
            return False
    return True