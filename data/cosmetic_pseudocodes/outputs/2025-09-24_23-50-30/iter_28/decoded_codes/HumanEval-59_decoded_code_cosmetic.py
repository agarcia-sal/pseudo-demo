from typing import Callable


def largest_prime_factor(p: int) -> int:
    def prime_check(q: int) -> bool:
        if q < 2:
            return False
        for idx in range(2, q):
            if q % idx == 0:
                return False
        return True

    top_factor: int = 1
    candidate: int = 2
    while candidate <= p:
        # Condition: (p % candidate == 0 and prime_check(candidate)) is True
        # FALSE = NOT(...) equivalent to: if (p % candidate == 0 and prime_check(candidate))
        if p % candidate == 0 and prime_check(candidate):
            top_factor = top_factor if top_factor > candidate else candidate
        candidate += 1

    return top_factor