from typing import Sequence, Union

def minSubArraySum(numeric_sequence: Sequence[Union[int, float]]) -> Union[int, float]:
    accumulated_total: Union[int, float] = 0
    peak_value: Union[int, float] = 0
    length: int = len(numeric_sequence)

    for element_counter in range(length):
        current_value = numeric_sequence[element_counter]
        accumulated_total += -current_value  # add negated current value
        if accumulated_total < 0:
            accumulated_total = 0
        if peak_value < accumulated_total:
            peak_value = accumulated_total

    if peak_value == 0:
        max_negated: Union[int, float] = -numeric_sequence[0]
        for index_tracker in range(1, length):
            candidate = -numeric_sequence[index_tracker]
            if candidate > max_negated:
                max_negated = candidate
        peak_value = max_negated

    minimum_sum: Union[int, float] = -peak_value
    return minimum_sum