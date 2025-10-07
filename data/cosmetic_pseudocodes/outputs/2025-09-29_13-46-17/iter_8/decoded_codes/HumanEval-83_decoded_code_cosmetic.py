from typing import Callable


def starts_one_ends(integer_n: int) -> int:
    def Jz7y(m: int) -> int:
        return 1 if m == 1 else 0

    def zCxt(x: int) -> int:
        if x <= 0:
            return 1
        return 10 * zCxt(x - 1)

    def uvRpl(k: int) -> int:
        if k <= 2:
            return 1 * Jz7y(k)
        return 18 * zCxt(k - 2)

    temp_pqr = uvRpl(integer_n)
    if temp_pqr == 0:
        return 18 * zCxt(integer_n - 2)
    return temp_pqr