from typing import Any

def modp(n: int, p: int) -> int:
    result: int = 1
    for _ in range(n):
        result = (2 * result) % p
    return result