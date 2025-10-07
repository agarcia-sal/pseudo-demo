from typing import Callable


def largest_prime_factor(x: int) -> int:
    def is_prime_number(y: int) -> bool:
        if y < 2:
            return False
        m = 2
        while m < y:
            if y % m == 0:
                return False
            m += 1
        return True

    candidate = 1
    index = 2
    while index <= x:
        if x % index == 0:
            if is_prime_number(index) and candidate < index:
                candidate = index
        index += 1
    return candidate