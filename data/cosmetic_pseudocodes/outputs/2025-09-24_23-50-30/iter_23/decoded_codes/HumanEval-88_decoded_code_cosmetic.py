from typing import List

def sort_array(sequence: List[int]) -> List[int]:
    if not sequence:
        return []
    edge_sum = sequence[0] + sequence[-1]
    descending_flag = (edge_sum % 2 == 0)
    return sorted(sequence, reverse=descending_flag)