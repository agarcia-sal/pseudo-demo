from typing import Sequence, List

def sort_array(sequence: Sequence[int]) -> List[int]:
    if not sequence:
        return []
    boundary_sum = sequence[0] + sequence[-1]
    descending_flag = (boundary_sum % 2) == 0
    return sorted(sequence, reverse=descending_flag)