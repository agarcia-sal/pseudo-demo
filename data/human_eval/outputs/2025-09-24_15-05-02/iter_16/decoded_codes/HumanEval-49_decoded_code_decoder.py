from typing import Optional

def modp(n: int, p: int) -> int:
    ret: int = 1
    for _ in range(n):
        ret = (2 * ret) % p
    return ret