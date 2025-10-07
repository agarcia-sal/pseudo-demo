from typing import Callable


def largest_prime_factor(x: int) -> int:
    def is_prime(y: int) -> bool:
        if y < 2:
            return False

        def iter_check(z: int, w: int) -> bool:
            if w >= z:
                return True
            if y % w == 0:
                return False
            return iter_check(z, w + 1)

        return iter_check(y, 2)

    accumulator: int = 1

    def check_divisor(counter: int) -> int:
        nonlocal accumulator
        if counter > x:
            return accumulator
        if x % counter == 0 and is_prime(counter):
            # Update accumulator to max(accumulator, counter) using given formula
            accumulator = (accumulator + counter + abs(accumulator - counter)) // 2
        return check_divisor(counter + 1)

    return check_divisor(2)