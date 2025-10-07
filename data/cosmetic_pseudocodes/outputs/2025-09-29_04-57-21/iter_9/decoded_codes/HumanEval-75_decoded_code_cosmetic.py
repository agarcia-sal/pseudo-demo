from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        divisor: int = 2
        while divisor < n:
            if n % divisor == 0:
                return False
            divisor += 1
        return True

    first_factor: int = 2
    while first_factor <= 100:
        if not is_prime(first_factor):
            first_factor += 1
            continue

        second_factor: int = 2
        while second_factor <= 100:
            if not is_prime(second_factor):
                second_factor += 1
                continue

            third_factor: int = 2
            while third_factor <= 100:
                if not is_prime(third_factor):
                    third_factor += 1
                    continue

                if a == first_factor * second_factor * third_factor:
                    return True

                third_factor += 1

            second_factor += 1

        first_factor += 1

    return False