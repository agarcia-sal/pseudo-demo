from math import floor
from typing import Union


def is_prime(value: int) -> bool:
    if value <= 1:
        return False
    counter: int = 2
    while counter <= value - 2:
        if value - floor(value / counter) * counter == 0:
            return False
        counter += 1
    return True