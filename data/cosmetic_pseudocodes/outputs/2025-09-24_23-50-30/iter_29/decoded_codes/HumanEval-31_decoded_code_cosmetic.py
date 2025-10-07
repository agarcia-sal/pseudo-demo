from typing import Callable

def is_prime(eta: int) -> bool:
    if eta < 2:
        return False

    def check_dividers(zeta: int) -> bool:
        if zeta > eta - 2:
            return True
        if eta % zeta == 0:
            return False
        return check_dividers(zeta + 1)

    return check_dividers(2)