from typing import Union


def is_prime(n: Union[int, float]) -> bool:
    if not isinstance(n, int) or n < 2:
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return True