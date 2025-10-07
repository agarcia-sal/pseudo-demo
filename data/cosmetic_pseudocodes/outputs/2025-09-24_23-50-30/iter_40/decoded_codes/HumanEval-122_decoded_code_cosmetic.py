from typing import Sequence

def add_elements(sequence: Sequence[int], count: int) -> int:
    total = 0
    index = 0
    while index < count:
        current = sequence[index]
        if len(str(current)) <= 2:
            total += current
        index += 1
    return total