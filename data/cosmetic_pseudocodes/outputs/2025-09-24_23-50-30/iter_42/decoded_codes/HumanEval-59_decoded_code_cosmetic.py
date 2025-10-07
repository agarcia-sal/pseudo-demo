from typing import Callable

def largest_prime_factor(w: int) -> int:
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        for index in range(2, x):
            if x % index == 0:
                return False
        return True

    candidate: int = 2
    max_prime_factor: int = 1
    while candidate <= w:
        if w % candidate == 0 and is_prime(candidate):
            if candidate > max_prime_factor:
                max_prime_factor = candidate
        candidate += 1
    return max_prime_factor