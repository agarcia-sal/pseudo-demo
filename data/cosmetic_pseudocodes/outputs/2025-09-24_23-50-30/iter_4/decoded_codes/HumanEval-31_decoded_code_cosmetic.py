from typing import Iterator

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    return not any(n % d == 0 for d in range(2, n))