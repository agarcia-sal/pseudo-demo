from typing import List


def count_up_to(n: int) -> List[int]:
    found_primes: List[int] = []

    def check_prime(candidate: int, divisor: int) -> bool:
        if divisor * divisor > candidate:
            return True
        if candidate % divisor == 0:
            return False
        return check_prime(candidate, divisor + 1)

    num: int = 2
    while num < n:
        if check_prime(num, 2):
            found_primes.append(num)
        num += 1

    return found_primes