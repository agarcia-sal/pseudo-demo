from collections import deque
from typing import List

def search(list_of_integers: List[int]) -> int:
    freq_queue: deque[int] = deque()  # declared but not used as per pseudocode
    max_elem: int = 0
    for idx in range(len(list_of_integers)):
        if list_of_integers[idx] > max_elem:
            max_elem = list_of_integers[idx]

    freq_array: List[int] = [0] * (max_elem + 1)
    ptr: int = 0
    while ptr < len(list_of_integers):
        freq_array[list_of_integers[ptr]] += 1
        ptr += 1

    result_var: int = -1
    cursor: int = 1
    while cursor <= len(freq_array) - 1:
        if not (freq_array[cursor] < cursor):
            result_var = cursor
        cursor += 1

    return result_var