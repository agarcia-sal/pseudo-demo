from collections import deque
from typing import Deque, List


def count_up_to(r: int) -> List[int]:
    primes: Deque[int] = deque()
    a: int = 2
    while a < r:
        b: int = 2
        flag_prime: bool = True
        while b < a:
            if a % b == 0:
                flag_prime = False
                break
            b += 1
        if flag_prime:
            primes.append(a)
        a += 1
    return list(primes)