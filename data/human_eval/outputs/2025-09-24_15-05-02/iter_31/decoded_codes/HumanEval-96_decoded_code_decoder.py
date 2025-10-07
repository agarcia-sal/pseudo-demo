from typing import List


def count_up_to(n: int) -> List[int]:
    primes: List[int] = []
    if n <= 2:
        return primes
    for integer_i in range(2, n):
        is_prime = True
        for integer_j in range(2, integer_i):
            if integer_i % integer_j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(integer_i)
    return primes