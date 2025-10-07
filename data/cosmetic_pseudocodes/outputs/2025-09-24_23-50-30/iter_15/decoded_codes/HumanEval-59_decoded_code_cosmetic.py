from collections import deque
from typing import List


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        # Check divisibility from 2 to k-1
        arr: List[int] = [x for x in range(2, k)]
        for idx in arr:
            if k % idx == 0:
                return False
        return True

    maxVal: int = 1
    divisorQueue: deque[int] = deque(range(2, n + 1))
    while divisorQueue:
        current = divisorQueue.popleft()
        if (n % current == 0) and is_prime(current):
            if current > maxVal:
                maxVal = current
    return maxVal