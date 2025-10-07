from typing import Sequence, Union


def minSubArraySum(input_sequence: Sequence[Union[int, float]]) -> Union[int, float]:
    idx_counter: int = 0
    accumulator: Union[int, float] = 0
    peak_value: Union[int, float] = 0

    while idx_counter < len(input_sequence):
        current_element = input_sequence[idx_counter]
        accumulator += -current_element
        if accumulator < 0:
            accumulator = 0
        if peak_value < accumulator:
            peak_value = accumulator
        idx_counter += 1

    if peak_value == 0:
        neg_values_array = [-x for x in input_sequence]
        peak_value = max(neg_values_array)

    result_value = -peak_value
    return result_value