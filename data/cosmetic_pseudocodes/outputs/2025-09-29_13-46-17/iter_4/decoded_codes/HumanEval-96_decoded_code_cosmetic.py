from typing import List

def count_up_to(n: int) -> List[int]:
    def check_prime(k: int, divisor: int) -> bool:
        if divisor * divisor > k:
            return True
        if k % divisor == 0:
            return False
        return check_prime(k, divisor + 1)

    def build_primes(current: int, limit: int, prime_accumulator: List[int]) -> List[int]:
        if current >= limit:
            return prime_accumulator
        if check_prime(current, 2):
            return build_primes(current + 1, limit, prime_accumulator + [current])
        return build_primes(current + 1, limit, prime_accumulator)

    return build_primes(2, n, [])