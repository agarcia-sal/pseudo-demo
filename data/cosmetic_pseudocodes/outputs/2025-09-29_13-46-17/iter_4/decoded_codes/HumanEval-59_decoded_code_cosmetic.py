from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False

        def check_divisor(x: int) -> bool:
            if x >= k:
                return True
            elif k % x == 0:
                return False
            else:
                return check_divisor(x + 1)

        return check_divisor(2)

    accumulator_max: int = 1

    # Use nonlocal to modify accumulator_max inside nested function
    def scan_divisor(candidate: int) -> int:
        nonlocal accumulator_max
        if candidate > n:
            return accumulator_max
        if n % candidate == 0 and is_prime(candidate):
            if candidate > accumulator_max:
                accumulator_max = candidate
        return scan_divisor(candidate + 1)

    return scan_divisor(2)