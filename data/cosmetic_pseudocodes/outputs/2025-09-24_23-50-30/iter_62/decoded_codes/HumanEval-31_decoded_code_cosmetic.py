from typing import Callable


def is_prime(value: int) -> bool:
    def check_factor(index: int) -> bool:
        if index > value - 2:
            return True
        if value % index == 0:
            return False
        return check_factor(index + 1)

    if value < 2:
        return False
    return check_factor(2)