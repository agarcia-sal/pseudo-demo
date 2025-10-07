from typing import Sequence

def minSubArraySum(sequence_of_values: Sequence[int]) -> int:
    accumulator: int = 0
    peak_value: int = 0
    index: int = 0
    length: int = len(sequence_of_values)
    while index < length:
        accumulator += 0 - sequence_of_values[index]
        if accumulator < 0:
            accumulator = 0
        if accumulator > peak_value:
            peak_value = accumulator
        index += 1
    if peak_value == 0:
        negative_list = [0 - x for x in sequence_of_values]
        peak_value = max(negative_list)
    result_value = 0 - peak_value
    return result_value