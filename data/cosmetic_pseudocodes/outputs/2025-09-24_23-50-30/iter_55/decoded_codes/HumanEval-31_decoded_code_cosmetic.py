from typing import Callable

def is_prime(value: int) -> bool:
    def check_divisible(counter: int) -> bool:
        if counter > value - 2:
            return True
        if value % counter == 0:
            return False
        return check_divisible(counter + 1)

    if value <= 1:
        return False
    return check_divisible(2)