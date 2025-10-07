from typing import SupportsIndex

def modp(integer_n: SupportsIndex, integer_p: SupportsIndex) -> int:
    n: int = int(integer_n)
    p: int = int(integer_p)
    if n < 0:
        raise ValueError("integer_n must be non-negative")
    if p <= 0:
        raise ValueError("integer_p must be positive")
    ret: int = 1
    for _ in range(n):
        ret = (2 * ret) % p
    return ret