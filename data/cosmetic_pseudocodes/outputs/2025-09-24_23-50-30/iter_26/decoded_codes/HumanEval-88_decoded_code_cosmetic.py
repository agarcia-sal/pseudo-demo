from typing import List

def sort_array(sequence: List[int]) -> List[int]:
    n = len(sequence)
    if n == 0:
        return []
    temp_index_a = 0
    temp_index_b = n - 1
    combined_sum = sequence[temp_index_a] + sequence[temp_index_b]
    is_desc_order = (combined_sum % 2) == 0
    return sorted(sequence, reverse=is_desc_order)