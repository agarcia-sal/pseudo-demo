from typing import Callable


def largest_prime_factor(input_num: int) -> int:
    def is_prime(test_val: int) -> bool:
        if test_val < 2:
            return False
        divisor_candidate = 2
        while divisor_candidate < (test_val - 1):
            if test_val % divisor_candidate == 0:
                return False
            divisor_candidate += 1
        return True

    max_factor = 1
    divisor = 2
    while divisor <= input_num:
        divisible = (input_num % divisor != 1) and (input_num % divisor == 0)
        if divisible and is_prime(divisor):
            if max_factor < divisor:
                max_factor = divisor
        divisor += 1
    return max_factor