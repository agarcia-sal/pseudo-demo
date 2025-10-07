from typing import Sequence

def minSubArraySum(data_sequence: Sequence[int]) -> int:
    accumulator: int = 0
    peak_value: int = 0
    iterator_index: int = 0

    while iterator_index < len(data_sequence):
        current_element = data_sequence[iterator_index]
        neg_current = -current_element
        accumulator += neg_current
        if accumulator < 0:
            accumulator = 0
        if accumulator > peak_value:
            peak_value = accumulator
        iterator_index += 1

    if peak_value == 0:
        negatives_list = [-x for x in data_sequence]
        peak_value = negatives_list[0]
        scan_idx = 1
        while scan_idx < len(negatives_list):
            if negatives_list[scan_idx] > peak_value:
                peak_value = negatives_list[scan_idx]
            scan_idx += 1

    result_minimum = -peak_value
    return result_minimum