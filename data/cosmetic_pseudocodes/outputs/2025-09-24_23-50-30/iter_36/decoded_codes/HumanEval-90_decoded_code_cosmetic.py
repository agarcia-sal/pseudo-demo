from collections import deque
from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    temp_queue: deque[int] = deque()
    for elem in list_of_integers:
        if elem not in temp_queue:
            temp_queue.append(elem)
    array_from_queue: List[int] = list(temp_queue)
    array_from_queue.sort()
    if len(array_from_queue) < 2:
        return None
    else:
        return array_from_queue[1]