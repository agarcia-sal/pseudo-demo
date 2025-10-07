from typing import Callable


def largest_prime_factor(m: int) -> int:
    def is_prime(p: int) -> bool:
        if p < 2:
            return False
        divisor_candidate = 2
        while divisor_candidate <= p - 1:
            if p % divisor_candidate == 0:
                return False
            divisor_candidate += 1
        return True

    current_largest_prime: int = 1
    factor_candidate: int = 2
    while factor_candidate <= m:
        if m % factor_candidate == 0:
            if is_prime(factor_candidate) and factor_candidate > current_largest_prime:
                current_largest_prime = factor_candidate
        factor_candidate += 1

    return current_largest_prime