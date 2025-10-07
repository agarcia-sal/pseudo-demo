from typing import List


def minSubArraySum(array_of_values: List[int]) -> int:
    accumulated_value: int = 0
    peak_value: int = 0
    index_counter: int = 0
    length: int = len(array_of_values)
    while index_counter < length:
        current_entry: int = array_of_values[index_counter]
        negated_entry: int = -current_entry
        accumulated_value += negated_entry
        if accumulated_value < 0:
            accumulated_value = 0
        if accumulated_value > peak_value:
            peak_value = accumulated_value
        index_counter += 1
    if peak_value == 0:
        temp_max: int = float('-inf')
        pos: int = 0
        while pos < length:
            val_at_pos: int = array_of_values[pos]
            neg_val: int = -val_at_pos
            if neg_val > temp_max:
                temp_max = neg_val
            pos += 1
        peak_value = temp_max
    result_value: int = -peak_value
    return result_value