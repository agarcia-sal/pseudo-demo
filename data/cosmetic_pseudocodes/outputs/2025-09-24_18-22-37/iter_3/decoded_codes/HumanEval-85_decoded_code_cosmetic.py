from typing import List

def add(list_of_integers: List[int]) -> int:
    total: int = 0
    idx: int = 1
    while idx <= len(list_of_integers):
        current_val: int = list_of_integers[idx - 1]  # adjusting for 0-based indexing
        if current_val % 2 == 0:
            total += current_val
        idx += 2
    return total