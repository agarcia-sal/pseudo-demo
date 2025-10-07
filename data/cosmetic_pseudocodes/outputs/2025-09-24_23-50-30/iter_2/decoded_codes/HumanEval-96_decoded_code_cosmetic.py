from typing import List
from collections import deque


def count_up_to(n: int) -> List[int]:
    primes: deque[int] = deque()

    def check_divisor(x: int, y: int) -> bool:
        if y * y > x:
            return True
        if x % y == 0:
            return False
        return check_divisor(x, y + 1)

    current_number = n - 1
    while current_number >= 2:
        if check_divisor(current_number, 2):
            primes.append(current_number)  # enqueue
        current_number -= 1

    result: List[int] = []
    while primes:
        result.append(primes.popleft())  # push onto result stack

    return result