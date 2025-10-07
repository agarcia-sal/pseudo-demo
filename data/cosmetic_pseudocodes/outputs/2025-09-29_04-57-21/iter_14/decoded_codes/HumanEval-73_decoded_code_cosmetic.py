from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    discrepancy_count: int = 0
    midpoint: int = len(array_of_integers) // 2
    cursor: int = 0

    while cursor < midpoint:
        left_val = array_of_integers[cursor]
        right_val = array_of_integers[len(array_of_integers) - cursor - 1]
        if left_val != right_val:
            discrepancy_count += 1
        cursor += 1

    return discrepancy_count