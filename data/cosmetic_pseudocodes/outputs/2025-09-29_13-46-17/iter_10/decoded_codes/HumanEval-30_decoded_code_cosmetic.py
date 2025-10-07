from collections import deque
from typing import List, Iterator

def get_positive(list_of_numbers: List[int]) -> List[int]:
    queue: deque[int] = deque()
    iterator: Iterator[int] = iter(list_of_numbers)
    while True:
        try:
            num = next(iterator)
        except StopIteration:
            break
        if num > 0:
            queue.append(num)
        # else continue is implicit by loop structure
    return list(queue)