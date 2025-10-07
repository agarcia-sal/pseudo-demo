from typing import Callable


def largest_prime_factor(number: int) -> int:
    def is_prime(check_num: int) -> bool:
        if check_num <= 1:
            return False

        def check_divisor(current: int) -> bool:
            if current >= check_num:
                return True
            if check_num % current == 0:
                return False
            return check_divisor(current + 1)

        return check_divisor(2)

    max_factor: int = 1
    factor_candidate: int = 2
    while factor_candidate <= number:
        if number % factor_candidate == 0 and is_prime(factor_candidate):
            if max_factor < factor_candidate:
                max_factor = factor_candidate
        factor_candidate += 1
    return max_factor