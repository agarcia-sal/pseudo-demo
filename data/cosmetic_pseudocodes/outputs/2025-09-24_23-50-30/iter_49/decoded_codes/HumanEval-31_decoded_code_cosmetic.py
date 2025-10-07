from typing import Callable

def is_prime(limb: int) -> bool:
    def perform_check(index: int) -> bool:
        if not (index <= limb - 2):
            return True
        if limb % index == 0:
            return False
        return perform_check(index + 1)

    return limb >= 2 and perform_check(2)