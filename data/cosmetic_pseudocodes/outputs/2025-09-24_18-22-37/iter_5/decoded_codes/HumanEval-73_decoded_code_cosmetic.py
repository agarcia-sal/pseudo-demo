from typing import List

def smallest_change(list_of_numbers: List[int]) -> int:
    mismatch_count: int = 0
    list_length: int = len(list_of_numbers)
    half_length: int = (list_length // 2) - 1
    current_pos: int = 0

    while current_pos <= half_length:
        start_elem: int = list_of_numbers[current_pos]
        end_elem_index: int = list_length - current_pos - 1
        end_elem: int = list_of_numbers[end_elem_index]

        if start_elem != end_elem:
            mismatch_count += 1

        current_pos += 1

    return mismatch_count