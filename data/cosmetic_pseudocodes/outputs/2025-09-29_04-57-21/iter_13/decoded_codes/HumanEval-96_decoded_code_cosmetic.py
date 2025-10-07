from typing import List


def count_up_to(n: int) -> List[int]:
    primes_collection: List[int] = []

    def verify_prime(candidate: int, divisor: int) -> bool:
        if divisor * divisor > candidate:
            return True
        if candidate % divisor == 0:
            return False
        return verify_prime(candidate, divisor + 1)

    index = 2
    while index < n:
        if verify_prime(index, 2):
            primes_collection.append(index)
        index += 1

    return primes_collection