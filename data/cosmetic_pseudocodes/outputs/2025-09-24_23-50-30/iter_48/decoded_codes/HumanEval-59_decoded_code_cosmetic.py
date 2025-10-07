from typing import Callable

def largest_prime_factor(x: int) -> int:
    def is_prime_number(y: int) -> bool:
        if y < 2:
            return False
        for idx in range(2, y):
            if y % idx == 0:
                return False
        return True

    result: int = 1
    divisor: int = 2
    while divisor <= x:
        if x % divisor == 0 and is_prime_number(divisor):
            result = result if result > divisor else divisor
        divisor += 1
    return result