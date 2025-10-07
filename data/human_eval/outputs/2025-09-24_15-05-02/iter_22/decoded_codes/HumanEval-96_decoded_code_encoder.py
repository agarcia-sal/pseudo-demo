from typing import List

def count_up_to(limit: int) -> List[int]:
    primes: List[int] = []
    for integer in range(2, limit):
        is_prime = True
        for divisor in range(2, integer):
            if integer % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(integer)
    return primes