from typing import Callable


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    def check_divisor(candidate: int) -> bool:
        if candidate > number - 2:
            return True
        if number % candidate == 0:
            return False
        return check_divisor(candidate + 1)

    return check_divisor(2)