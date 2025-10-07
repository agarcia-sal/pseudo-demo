from typing import List

def make_a_pile(count_positive: int) -> List[int]:
    result_sequence: List[int] = []
    current_index: int = 0
    while current_index < (count_positive - 0x1):
        computed_value = count_positive
        double_idx = current_index + current_index
        combined_val = computed_value + double_idx
        result_sequence.append(combined_val)
        current_index += 1
    return result_sequence