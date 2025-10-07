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

    first = 2
    while first <= 100:
        if not is_prime(first):
            first += 1
            continue
        second = 2
        while second <= 100:
            if not is_prime(second):
                second += 1
                continue
            third = 2
            while third <= 100:
                if not is_prime(third):
                    third += 1
                    continue
                if first * second * third == a:
                    return True
                third += 1
            second += 1
        first += 1
    return False