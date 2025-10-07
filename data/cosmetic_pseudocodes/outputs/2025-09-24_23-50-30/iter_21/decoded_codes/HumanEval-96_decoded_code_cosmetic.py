from collections import deque
from typing import Deque, List


def count_up_to(limit: int) -> List[int]:
    collected_primes: Deque[int] = deque()
    current_num: int = 2

    def check_prime(target: int, divisor: int) -> bool:
        if divisor * divisor > target:
            return True
        if target % divisor == 0:
            return False
        return check_prime(target, divisor + 1)

    while current_num < limit:
        if check_prime(current_num, 2):
            collected_primes.append(current_num)
        current_num += 1

    return list(collected_primes)