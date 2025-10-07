from typing import List


def count_up_to(x: int) -> List[int]:
    primes_container: List[int] = []

    def check_divisor(candidate: int, divisor: int) -> bool:
        while divisor < candidate:
            if candidate % divisor == 0:
                return False
            divisor += 1
        return True

    y: int = 2
    while y < x:
        if check_divisor(y, 2):
            primes_container.append(y)
        y += 1

    return primes_container