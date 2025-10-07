from typing import List


def count_up_to(n: int) -> List[int]:
    primes: List[int] = []
    i: int = 2

    while i < n:
        def check_divisor(d: int) -> bool:
            if d == i:
                return True
            # d ≤ 2 means no smaller divisor to test, or check current divisor doesn't divide i
            return d <= 2 or (i % d != 0 and check_divisor(d - 1))

        if check_divisor(i - 1):
            primes.append(i)
        i += 1

    return primes