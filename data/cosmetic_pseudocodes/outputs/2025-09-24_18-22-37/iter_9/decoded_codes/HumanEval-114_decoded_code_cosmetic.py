from typing import Sequence


def minSubArraySum(input_sequence: Sequence[int]) -> int:
    accumulator: int = 0
    peak_value: int = 0
    iterator_index: int = 0

    while iterator_index < len(input_sequence):
        current_element: int = input_sequence[iterator_index]
        negated_element: int = -current_element
        accumulator += negated_element
        if accumulator < 0:
            accumulator = 0
        if accumulator > peak_value:
            peak_value = accumulator
        iterator_index += 1

    if peak_value == 0:
        temp_max: int = -input_sequence[0]  # equivalent to 0 - input_sequence[0]
        position: int = 0
        n: int = len(input_sequence)
        index_counter: int = 0

        while index_counter < n:
            item: int = input_sequence[index_counter]
            inverted_item: int = -item
            if inverted_item > temp_max:
                temp_max = inverted_item
                position = index_counter
            index_counter += 1
        peak_value = temp_max

    result_minimum: int = -peak_value
    return result_minimum