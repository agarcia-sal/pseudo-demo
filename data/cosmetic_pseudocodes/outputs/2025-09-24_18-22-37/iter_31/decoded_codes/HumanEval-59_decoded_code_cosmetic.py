from typing import Union

def largest_prime_factor(x: int) -> int:
    def is_prime_number(y: int) -> bool:
        if y < 2:
            return False
        p = 2
        while p < y:
            if y % p == 0:
                return False
            p += 1
        return True

    max_factor = 1
    factor_candidate = 2
    while factor_candidate <= x:
        if x % factor_candidate == 0:
            if is_prime_number(factor_candidate):
                max_factor = max(max_factor, factor_candidate)
        factor_candidate += 1
    return max_factor