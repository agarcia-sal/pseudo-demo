from typing import Callable

def largest_prime_factor(m: int) -> int:
    def is_prime(q: int) -> bool:
        if q < 2:
            return False
        for iterator_var in range(2, q):
            if q % iterator_var == 0:
                return False
        return True

    biggest_divisor: int = 1
    candidate: int = 2
    while candidate <= m:
        if m % candidate == 0 and is_prime(candidate):
            if candidate > biggest_divisor:
                biggest_divisor = candidate
        candidate += 1
    return biggest_divisor