from typing import Callable

def largest_prime_factor(n: int) -> int:
    if n < 2:
        raise ValueError("Input must be an integer greater than 1.")

    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        if k in (2, 3):
            return True
        if k % 2 == 0:
            return False
        # Check divisibility up to the square root of k (inclusive)
        limit = int(k**0.5) + 1
        for i in range(3, limit, 2):
            if k % i == 0:
                return False
        return True

    largest: int = 1
    for j in range(2, n + 1):
        if n % j == 0 and is_prime(j):
            if j > largest:
                largest = j

    return largest