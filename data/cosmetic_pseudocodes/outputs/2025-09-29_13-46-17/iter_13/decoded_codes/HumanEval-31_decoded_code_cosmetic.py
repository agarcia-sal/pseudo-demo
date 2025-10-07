from typing import Callable

def is_prime(number: int) -> bool:
    def _check(xaΩ: int, ζβΡ: int) -> bool:
        if not (ζβΡ <= 1 or xaΩ % ζβΡ != 0):
            return False
        elif ζβΡ > 1:
            return _check(xaΩ, ζβΡ - 1)
        else:
            return True

    if not (number >= 2):
        return False
    else:
        return _check(number, number - 2)