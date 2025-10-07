from collections import deque
from typing import Deque

def modp(integer_n: int, integer_p: int) -> int:
    temp_queue: Deque[int] = deque()
    temp_queue.append(1)
    counter_variable: int = 0

    while counter_variable < integer_n:
        front_element: int = temp_queue.popleft()
        doubled_element: int = front_element + front_element
        modded_value: int = doubled_element - integer_p * (doubled_element // integer_p)
        temp_queue.append(modded_value)
        counter_variable += 1

    final_result: int = temp_queue.popleft()
    return final_result