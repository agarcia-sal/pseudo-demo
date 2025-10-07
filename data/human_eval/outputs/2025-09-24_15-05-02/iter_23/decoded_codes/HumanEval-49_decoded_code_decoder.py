from typing import SupportsIndex

def modp(n: SupportsIndex, p: SupportsIndex) -> int:
    n_int = n.__index__()
    p_int = p.__index__()
    if n_int < 0 or p_int <= 0:
        raise ValueError("n must be non-negative and p must be a positive integer")
    result: int = 1
    for _ in range(n_int):
        result = (2 * result) % p_int
    return result