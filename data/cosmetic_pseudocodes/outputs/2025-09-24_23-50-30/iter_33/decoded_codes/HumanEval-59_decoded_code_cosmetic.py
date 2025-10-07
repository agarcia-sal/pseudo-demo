from typing import Callable


def largest_prime_factor(n_input: int) -> int:
    def is_prime(test_num: int) -> bool:
        if test_num < 2:
            return False

        def check_division(x: int) -> bool:
            if x >= test_num:
                return True
            if test_num % x == 0:
                return False
            return check_division(x + 1)

        return check_division(2)

    candidate = 2
    current_largest = 1
    while candidate <= n_input:
        if n_input % candidate == 0:
            if is_prime(candidate):
                if candidate > current_largest:
                    current_largest = candidate
        candidate += 1
    return current_largest