from collections import deque
from typing import List, Optional


def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    temp_queue: deque[int] = deque()
    temp_set: set[int] = set()

    for ch in list_of_integers:
        if ch not in temp_set:
            temp_queue.append(ch)
            temp_set.add(ch)

    arr_temp: List[int] = [temp_queue.popleft() for _ in range(len(temp_queue))]

    arr_temp.sort()

    if not (len(arr_temp) - 2 >= 0):
        return None

    result_val: int = arr_temp[1]
    return result_val