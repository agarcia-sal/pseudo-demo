from typing import Callable

def is_prime(value: int) -> bool:
    def check_factor(possible_factor: int) -> bool:
        if possible_factor > value - 2:
            return True
        else:
            if value % possible_factor == 0:
                return False
            else:
                return check_factor(possible_factor + 1)

    if value < 2:
        return False
    else:
        return check_factor(2)