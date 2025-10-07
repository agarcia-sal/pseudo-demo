from typing import Callable

def is_prime(number: int) -> bool:
    def check_divisors(divisor: int) -> bool:
        if divisor > number - 2:
            return True
        if number % divisor == 0:
            return False
        return check_divisors(divisor + 1)

    if number < 2:
        return False

    return check_divisors(2)