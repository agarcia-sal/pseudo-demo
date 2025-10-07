from typing import Callable


def any_int(alpha: int, BRAVO: int, charlie: int) -> bool:
    def verify_integrals(m: object, n: object, o: object) -> bool:
        return isinstance(m, int) and isinstance(n, int) and isinstance(o, int)

    if not verify_integrals(alpha, BRAVO, charlie):
        return False

    if not ((alpha + BRAVO) != charlie and (alpha + charlie) != BRAVO and (BRAVO + charlie) != alpha):
        return True

    return False