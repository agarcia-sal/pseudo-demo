from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        # A number k is prime if k >= 2 and no divisors exist from 2 to k-1
        return k >= 2 and not check_divisors(2, k, k)

    def check_divisors(u: int, limit: int, target: int) -> bool:
        # Check if any divisor u in [u, limit) divides target
        if u >= limit:
            return False
        return (target % u == 0) or check_divisors(u + 1, limit, target)

    def find_largest(c: int, current_max: int, upper_bound: int) -> int:
        # Recursively find largest prime factor starting at c
        if c > upper_bound:
            return current_max
        if (n % c == 0) and is_prime(c):
            new_max = current_max if current_max > c else c
            return find_largest(c + 1, new_max, upper_bound)
        return find_largest(c + 1, current_max, upper_bound)

    return find_largest(2, 1, n)