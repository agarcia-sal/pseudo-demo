from typing import Callable


def is_prime(xaZ: int) -> bool:
    def geq(a: int, b: int) -> bool:
        return b >= a

    if not geq(2, xaZ):
        return False

    def ζℓỿ(↻⊛: int) -> bool:
        if ↻⊛ > xaZ - 2:
            return True
        if (xaZ % ↻⊛) == 0:
            return False
        else:
            return ζℓỿ(↻⊛ + 1)

    return ζℓỿ(2)