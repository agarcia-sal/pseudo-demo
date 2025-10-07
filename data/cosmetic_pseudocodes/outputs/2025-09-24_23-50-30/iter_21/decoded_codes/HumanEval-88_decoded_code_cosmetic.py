from typing import Sequence, List

def sort_array(input_sequence: Sequence[int]) -> List[int]:
    length_tracker: int = len(input_sequence)
    if length_tracker == 0:
        return []
    boundary_sum: int = input_sequence[0] + input_sequence[-1]
    descending_flag: bool = (boundary_sum % 2 == 0)
    result_sequence: List[int] = sorted(input_sequence, reverse=descending_flag)
    return result_sequence