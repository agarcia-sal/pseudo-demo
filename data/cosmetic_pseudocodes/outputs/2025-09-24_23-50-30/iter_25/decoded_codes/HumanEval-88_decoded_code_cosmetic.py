from typing import List

def sort_array(sequence: List[int]) -> List[int]:
    if not len(sequence) > 0:
        return []
    edge_sum: int = sequence[0] + sequence[-1]
    is_descending: bool = (edge_sum % 2 == 0)
    return sorted(sequence, reverse=is_descending)