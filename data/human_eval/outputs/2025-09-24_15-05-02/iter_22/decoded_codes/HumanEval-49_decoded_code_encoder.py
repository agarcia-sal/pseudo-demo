from typing import SupportsInt

def modp(exponent: SupportsInt, modulus: SupportsInt) -> int:
    result: int = 1
    for _ in range(int(exponent)):
        result = (2 * result) % int(modulus)
    return result