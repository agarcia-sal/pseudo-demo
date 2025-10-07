from typing import Callable

def is_prime(value: int) -> bool:
    def check_divisor(current_divisor: int, limit: int, found_divisor: bool) -> bool:
        if found_divisor:
            return False
        if current_divisor > limit:
            return True
        return check_divisor(current_divisor + 1, limit, value % current_divisor == 0)

    if value < 2:
        return False
    return check_divisor(2, value - 2, False)