from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        def checker(z: int, w: int) -> bool:
            if w >= z:
                return True
            if k % w == 0:
                return False
            return checker(z, w + 1)

        if k < 2:
            return False
        return checker(k, 2)

    def cmp(a: int, b: int) -> int:
        return a if a > b else b

    def finder(x: int, acc: int) -> int:
        if x > n:
            return acc
        if n % x == 0:
            # If x is prime and greater than acc, update acc; otherwise keep acc
            acc = cmp(acc, x if is_prime(x) else acc)
        return finder(x + 1, acc)

    return finder(2, 1)