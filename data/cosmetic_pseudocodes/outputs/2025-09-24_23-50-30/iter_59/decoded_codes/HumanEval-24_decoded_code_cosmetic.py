from collections import deque
from typing import Optional

def largest_divisor(integer_n: int) -> Optional[int]:
    def find_divisor(queue_x: deque[int]) -> Optional[int]:
        if not queue_x:
            return None
        queue_y = queue_x.popleft()
        if integer_n % queue_y == 0:
            return queue_y
        return find_divisor(queue_x)

    list_z = list(range(integer_n - 1, 0, -1))
    return find_divisor(deque(list_z))