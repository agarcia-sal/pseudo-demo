from typing import Callable

def largest_prime_factor(n: int) -> int:
    def helper_is_prime(k: int) -> bool:
        if k < 2:
            return False
        def recur_check(m: int) -> bool:
            if m == k:
                return True
            return (k % m != 0) and recur_check(m + 1)
        return recur_check(2)

    def gather_candidates(x: int, y: int, acc: int) -> int:
        if y > x:
            return acc
        acc2 = y if (x % y == 0 and helper_is_prime(y) and y > acc) else acc
        return gather_candidates(x, y + 1, acc2)

    return gather_candidates(n, 2, 1)