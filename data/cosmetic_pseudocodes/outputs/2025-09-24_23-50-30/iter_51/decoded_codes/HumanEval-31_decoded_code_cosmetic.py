from typing import Callable


def is_prime(value: int) -> bool:
    def check_divide(candidate: int, limit: int) -> bool:
        if candidate > limit:
            return True
        elif value % candidate == 0:
            return False
        else:
            return check_divide(candidate + 1, limit)

    return (value >= 2) and check_divide(2, value - 2)