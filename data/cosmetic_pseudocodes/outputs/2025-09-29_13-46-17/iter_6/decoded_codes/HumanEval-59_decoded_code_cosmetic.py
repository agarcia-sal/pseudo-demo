from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False

        def check_divisor(x: int) -> bool:
            if x >= k:
                return True
            if k % x == 0:
                return False
            return check_divisor(x + 1)

        return check_divisor(2)

    def update_largest(j: int, current_max: int) -> int:
        if j > n:
            return current_max
        is_divisor = (n % j == 0)
        prime_check = int(is_prime(j))
        condition_met = is_divisor * prime_check
        next_max = current_max
        if condition_met == 1:
            next_max = max(current_max, j)
        return update_largest(j + 1, next_max)

    return update_largest(2, 1)