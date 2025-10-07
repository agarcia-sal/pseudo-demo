from typing import Sequence

def smallest_change(data_sequence: Sequence) -> int:
    total_discrepancies = 0
    half_point = (len(data_sequence) // 2) - 1
    counter = 0
    while counter <= half_point:
        left_val = data_sequence[counter]
        right_index = len(data_sequence) - counter - 1
        right_val = data_sequence[right_index]
        if left_val != right_val:
            total_discrepancies += 1
        counter += 1
    return total_discrepancies