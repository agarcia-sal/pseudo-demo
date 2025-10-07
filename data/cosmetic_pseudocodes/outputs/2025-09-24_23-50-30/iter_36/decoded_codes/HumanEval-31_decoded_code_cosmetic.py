from typing import Callable


def is_prime(value: int) -> bool:
    if value < 2:
        return False

    def check_division(current: int) -> bool:
        if current > value - 2:
            return True
        if value % current == 0:
            return False
        return check_division(current + 1)

    return check_division(2)