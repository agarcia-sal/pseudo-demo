from typing import Sequence, List

def sort_array(input_sequence: Sequence[int]) -> List[int]:
    length = len(input_sequence)
    if length == 0:
        return []
    boundary_sum = input_sequence[0] + input_sequence[length - 1]
    descending_flag = (boundary_sum % 2 == 0)
    return sorted(input_sequence, reverse=descending_flag)