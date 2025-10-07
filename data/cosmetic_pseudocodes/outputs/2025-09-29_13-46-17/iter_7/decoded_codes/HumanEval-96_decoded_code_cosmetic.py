from typing import List

def count_up_to(n: int) -> List[int]:
    def accumulate_primes(x: int, limit: int, aggregated_primes: List[int]) -> List[int]:
        if not (x < limit):
            return aggregated_primes
        elif check_prime(x, 2):
            return accumulate_primes(x + 1, limit, aggregated_primes + [x])
        else:
            return accumulate_primes(x + 1, limit, aggregated_primes)

    def check_prime(candidate: int, divisor: int) -> bool:
        if not (divisor * divisor <= candidate):
            return True
        else:
            if candidate % divisor == 0:
                return False
            else:
                return check_prime(candidate, divisor + 1)

    return accumulate_primes(2, n, [])