from typing import Callable

def is_multiply_prime(a: int) -> bool:
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for factor in range(2, int(num ** 0.5) + 1):
            if num % factor == 0:
                return False
        return True

    primes = [p for p in range(2, 101) if is_prime(p)]
    for candidate_i in primes:
        for candidate_j in primes:
            for candidate_k in primes:
                if candidate_i * candidate_j * candidate_k == a:
                    return True
    return False