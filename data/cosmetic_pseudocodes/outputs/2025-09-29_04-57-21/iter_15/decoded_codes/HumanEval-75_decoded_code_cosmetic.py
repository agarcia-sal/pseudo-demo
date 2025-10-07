from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        divisor = 2
        while divisor < n:
            if n % divisor == 0:
                return False
            divisor += 1
        return True

    first_candidate = 2
    while first_candidate <= 100:
        if not is_prime(first_candidate):
            first_candidate += 1
            continue
        second_candidate = 2
        while second_candidate <= 100:
            if not is_prime(second_candidate):
                second_candidate += 1
                continue
            third_candidate = 2
            while third_candidate <= 100:
                if not is_prime(third_candidate):
                    third_candidate += 1
                    continue
                if a == first_candidate * second_candidate * third_candidate:
                    return True
                third_candidate += 1
            second_candidate += 1
        first_candidate += 1
    return False