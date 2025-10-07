from typing import List

def sort_array(sequence: List[int]) -> List[int]:
    if len(sequence) == 0:
        return []
    boundary_sum = sequence[0] + sequence[-1]
    order_descending = (boundary_sum % 2 == 0)
    return sorted(sequence, reverse=order_descending)