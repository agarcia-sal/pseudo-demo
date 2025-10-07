from typing import Union


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    limit: int = int(n**0.5) + 1
    for k in range(3, limit, 2):
        if n % k == 0:
            return False
    return True