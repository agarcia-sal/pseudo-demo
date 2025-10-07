from typing import List

def sort_array(sequence: List[int]) -> List[int]:
    if not sequence:
        return []
    boundary_sum: int = sequence[-1] + sequence[0]
    descending_flag: bool = (boundary_sum % 2 == 0)
    return sorted(sequence, reverse=descending_flag)