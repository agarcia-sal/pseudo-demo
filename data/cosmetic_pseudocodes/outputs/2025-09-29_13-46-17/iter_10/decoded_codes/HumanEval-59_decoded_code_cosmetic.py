from functools import reduce
from typing import Callable

def largest_prime_factor(n: int) -> int:
    def is_prime(z: int) -> bool:
        if z < 2:
            return False
        # foldl((∀ς→ς≠0), ζƶ-1, lambda) means: check all i in range 2..z-1 that z % i != 0
        # The lambda returns False if z % i == 0 or if i < 2 (which never occurs in this range),
        # else returns the accumulator (ɲ), starting True.
        def fold_fn(acc: bool, p: int) -> bool:
            if p < 2:
                return False
            if z % p == 0:
                return False
            return acc
        return reduce(fold_fn, range(z - 1, 1, -1), True)

    one = 1
    def s(x: int, y: int) -> int:
        return x if x > y else y

    def toward_largest(x: int, y: int) -> int:
        if n % y == 0 and is_prime(y):
            return s(x, y)
        return x

    # foldr(toward_largest, one, [2..n]) reduces from right to left over 2..n,
    # updating the accumulator with the largest prime factor found
    # But since s and toward_largest are commutative/max functions, foldr or foldl is equivalent here.
    result = reduce(toward_largest, reversed(range(2, n + 1)), one)
    return result