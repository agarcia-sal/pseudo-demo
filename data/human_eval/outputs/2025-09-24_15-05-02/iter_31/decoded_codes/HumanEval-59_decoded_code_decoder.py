from typing import Optional


def largest_prime_factor(integer_n: int) -> int:
    def is_prime(integer_k: int) -> bool:
        if integer_k < 2:
            return False
        if integer_k == 2:
            return True
        if integer_k % 2 == 0:
            return False
        for integer_i in range(3, int(integer_k**0.5) + 1, 2):
            if integer_k % integer_i == 0:
                return False
        return True

    if integer_n < 2:
        return 1

    largest = 1
    for integer_j in range(2, integer_n + 1):
        if integer_n % integer_j == 0 and is_prime(integer_j):
            largest = max(largest, integer_j)
    return largest