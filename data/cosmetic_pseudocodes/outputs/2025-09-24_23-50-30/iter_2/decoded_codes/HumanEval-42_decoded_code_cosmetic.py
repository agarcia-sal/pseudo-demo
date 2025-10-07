from collections import deque
from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    result_list: deque[int] = deque()
    i: int = 0
    while i < len(list_of_elements):
        result_list.append(list_of_elements[i] + 1)
        i += 1
    return list(result_list)