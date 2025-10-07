from typing import Callable

def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        # Check divisibility up to sqrt(k) for efficiency
        limit = int(k**0.5)
        return not any(k % i == 0 for i in range(2, limit + 1))

    def find_largest_divisor(current: int, limit: int, acc: int) -> int:
        if current > limit:
            return acc
        if n % current == 0 and is_prime(current) and current > acc:
            acc = current
        return find_largest_divisor(current + 1, limit, acc)

    return find_largest_divisor(2, n, 1)