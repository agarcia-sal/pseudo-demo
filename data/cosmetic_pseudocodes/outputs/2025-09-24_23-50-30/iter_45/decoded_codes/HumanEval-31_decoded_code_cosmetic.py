from typing import Callable


def is_prime(value: int) -> bool:
    def check_factor(candidate: int) -> bool:
        if candidate > value - 2:
            return True
        if value % candidate == 0:
            return False
        return check_factor(candidate + 1)

    if value < 2:
        return False
    return check_factor(2)