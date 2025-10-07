from typing import List

def count_up_to(n: int) -> List[int]:
    def check_prime(candidate: int, divisor: int) -> bool:
        if divisor * divisor > candidate:
            return True
        if candidate % divisor == 0:
            return False
        return check_prime(candidate, divisor + 1)

    def accumulate_primes(current: int, limit: int, collected: List[int]) -> List[int]:
        if current >= limit:
            return collected
        if check_prime(current, 2):
            return accumulate_primes(current + 1, limit, collected + [current])
        return accumulate_primes(current + 1, limit, collected)

    return accumulate_primes(2, n, [])