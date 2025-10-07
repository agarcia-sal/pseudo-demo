from typing import List

def count_up_to(n: int) -> List[int]:
    primes: List[int] = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes