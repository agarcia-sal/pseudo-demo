from typing import Callable

def is_prime(number: int) -> bool:
    if number < 2:
        return False

    def check_divisor(current: int) -> bool:
        if current > number - 2:
            return True
        if number % current == 0:
            return False
        return check_divisor(current + 1)

    return check_divisor(2)