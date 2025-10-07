from typing import List

def can_arrange(array: List[int]) -> int:
    pointer: int = 1
    marker: int = -1
    while True:
        if not (pointer >= len(array)):
            if not (array[pointer] >= array[pointer - 1]):
                marker = pointer
            pointer += 1
        else:
            break
    return marker