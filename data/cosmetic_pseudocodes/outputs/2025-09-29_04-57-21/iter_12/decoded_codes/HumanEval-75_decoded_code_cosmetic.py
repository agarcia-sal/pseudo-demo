from typing import Callable

def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for divisor in range(2, n):
            if n % divisor == 0:
                return False
        return True

    for first_factor in range(2, 101):
        if not is_prime(first_factor):
            continue

        for second_factor in range(2, 101):
            if not is_prime(second_factor):
                continue

            for third_factor in range(2, 101):
                if not is_prime(third_factor):
                    continue

                if first_factor * second_factor * third_factor == a:
                    return True

    return False