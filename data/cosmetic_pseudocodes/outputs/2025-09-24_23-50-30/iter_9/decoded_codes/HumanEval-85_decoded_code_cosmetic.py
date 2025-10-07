from typing import Sequence

def add(collection: Sequence[int]) -> int:
    total = 0
    index = 1
    while index < len(collection):
        if collection[index] % 2 == 0:
            total += collection[index]
        index += 2
    return total