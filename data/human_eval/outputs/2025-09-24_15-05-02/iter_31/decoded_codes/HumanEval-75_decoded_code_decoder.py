from typing import Callable


def is_multiply_prime(integer_a: int) -> bool:
    def is_prime(integer_n: int) -> bool:
        if integer_n < 2:
            return False
        if integer_n == 2:
            return True
        if integer_n % 2 == 0:
            return False
        # Check only odd divisors up to sqrt(integer_n)
        limit = int(integer_n**0.5) + 1
        for integer_j in range(3, limit, 2):
            if integer_n % integer_j == 0:
                return False
        return True

    if integer_a < 8:  # Minimum product of three primes >= 2*2*2 =8
        return False

    for integer_i in range(2, 101):
        if not is_prime(integer_i):
            continue
        for integer_j in range(2, 101):
            if not is_prime(integer_j):
                continue
            for integer_k in range(2, 101):
                if not is_prime(integer_k):
                    continue
                if integer_i * integer_j * integer_k == integer_a:
                    return True
    return False