from typing import List

def add(lst: List[int]) -> int:
    total = 0
    length = len(lst)
    i = 1
    while i < length:
        if lst[i] % 2 == 0:
            total += lst[i]
        i += 2
    return total