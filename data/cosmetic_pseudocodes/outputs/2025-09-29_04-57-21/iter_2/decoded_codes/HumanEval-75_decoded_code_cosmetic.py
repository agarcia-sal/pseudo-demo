from typing import Callable


def is_multiply_prime(value: int) -> bool:
    def is_prime(check: int) -> bool:
        if check < 2:
            return False
        for divisor_candidate in range(2, int(check**0.5) + 1):
            if check % divisor_candidate == 0:
                return False
        return True

    for first_factor in range(2, 101):
        if not is_prime(first_factor):
            continue
        for second_factor in range(2, 101):
            if not is_prime(second_factor):
                continue
            for candidate_factor in range(2, 101):
                if not is_prime(candidate_factor):
                    continue
                if first_factor * second_factor * candidate_factor == value:
                    return True
    return False