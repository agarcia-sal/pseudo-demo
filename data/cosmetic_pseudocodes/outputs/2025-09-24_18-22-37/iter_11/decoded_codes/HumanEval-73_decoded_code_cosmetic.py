from typing import Sequence

def smallest_change(sequence_of_nums: Sequence[int]) -> int:
    total_changes: int = 0
    max_index: int = (len(sequence_of_nums) // 2) - 1
    iterator: int = 0

    while iterator <= max_index:
        left_elem: int = sequence_of_nums[iterator]
        right_elem_to_compare_to: int = sequence_of_nums[len(sequence_of_nums) - iterator - 1]
        if left_elem != right_elem_to_compare_to:
            total_changes += 1
        iterator += 1

    return total_changes