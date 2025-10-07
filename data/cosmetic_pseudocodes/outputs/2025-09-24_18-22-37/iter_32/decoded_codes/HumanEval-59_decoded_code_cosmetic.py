from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k_var: int) -> bool:
        if k_var < 2:
            return False
        divisor_candidate = 2
        while divisor_candidate < k_var - 1:
            if k_var % divisor_candidate == 0:
                return False
            divisor_candidate += 1
        return True

    max_factor = 1
    current_divisor = 2
    while current_divisor <= n:
        if n % current_divisor == 0:
            if is_prime(current_divisor):
                if current_divisor > max_factor:
                    max_factor = current_divisor
        current_divisor += 1
    return max_factor