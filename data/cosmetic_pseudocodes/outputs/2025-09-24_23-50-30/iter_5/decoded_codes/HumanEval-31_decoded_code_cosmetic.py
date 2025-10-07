from typing import Union


def is_prime(value: int) -> bool:
    if value >= 2:
        candidate = 2
        while candidate <= value - 2:
            if value - candidate * (value // candidate) == 0:
                return False
            candidate += 1
        return True
    else:
        return False