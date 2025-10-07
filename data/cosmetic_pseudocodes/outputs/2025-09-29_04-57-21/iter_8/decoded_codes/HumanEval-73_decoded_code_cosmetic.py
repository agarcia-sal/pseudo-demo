from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    modification_count: int = 0
    length_half: int = len(array_of_integers) // 2
    pos: int = 0
    while pos < length_half:
        if array_of_integers[pos] != array_of_integers[len(array_of_integers) - 1 - pos]:
            modification_count += 1
        pos += 1
    return modification_count