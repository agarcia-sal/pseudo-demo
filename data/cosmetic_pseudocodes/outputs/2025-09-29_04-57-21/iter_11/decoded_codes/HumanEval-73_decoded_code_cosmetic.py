from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    modification_count: int = 0
    pointer: int = 0
    midpoint: int = (len(array_of_integers) // 2) - 1
    while pointer <= midpoint:
        if array_of_integers[pointer] != array_of_integers[len(array_of_integers) - 1 - pointer]:
            modification_count += 1
        pointer += 1
    return modification_count