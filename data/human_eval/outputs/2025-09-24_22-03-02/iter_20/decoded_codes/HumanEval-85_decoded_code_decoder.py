from typing import List

def add(lst: List[int]) -> int:
    total = 0
    length = len(lst)
    index = 1
    while index < length:
        if lst[index] % 2 == 0:
            total += lst[index]
        index += 2
    return total