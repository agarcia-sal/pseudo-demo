from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    mismatch_count: int = 0
    max_check_index: int = (len(array_of_integers) - 1) // 2
    current_index: int = 0
    while current_index <= max_check_index:
        if array_of_integers[current_index] != array_of_integers[len(array_of_integers) - 1 - current_index]:
            mismatch_count += 1
        current_index += 1
    return mismatch_count