from typing import Callable

def largest_prime_factor(x: int) -> int:
    def is_prime(y: int) -> bool:
        def check_divisor(z: int, limit: int) -> bool:
            if z > limit:
                return True
            if y % z == 0:
                return False
            return check_divisor(z + 1, limit)
        return (y > 1) and check_divisor(2, y - 1)

    def iterate_divisors(current: int, maximum: int, record: int) -> int:
        if current > maximum:
            return record
        if x % current == 0 and is_prime(current) and current > record:
            record = current
        return iterate_divisors(current + 1, maximum, record)

    return iterate_divisors(2, x, 1)