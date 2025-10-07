from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        if k in (2, 3):
            return True
        if k % 2 == 0 or k % 3 == 0:
            return False
        i = 5
        while i * i <= k:
            if k % i == 0 or k % (i + 2) == 0:
                return False
            i += 6
        return True

    largest = 1
    j = 2
    while j <= n:
        if n % j == 0 and is_prime(j):
            if j > largest:
                largest = j
        j += 1
    return largest