from typing import Sequence, Union

def minSubArraySum(input_sequence: Sequence[Union[int, float]]) -> Union[int, float]:
    greatest_total: Union[int, float] = 0
    current_accumulator: Union[int, float] = 0
    iterator_index: int = 0

    while iterator_index < len(input_sequence):
        element_value = input_sequence[iterator_index]
        negated_element = -element_value
        current_accumulator += negated_element

        if current_accumulator < 0:
            current_accumulator = 0

        if greatest_total < current_accumulator:
            greatest_total = current_accumulator

        iterator_index += 1

    if greatest_total == 0:
        negated_values = []
        position_counter = 0

        while position_counter < len(input_sequence):
            item = input_sequence[position_counter]
            negated_item = -item
            negated_values.append(negated_item)
            position_counter += 1

        highest_negated_value = negated_values[0]
        negated_index = 1

        while negated_index < len(negated_values):
            if negated_values[negated_index] > highest_negated_value:
                highest_negated_value = negated_values[negated_index]
            negated_index += 1

        greatest_total = highest_negated_value

    minimal_sum_result = -greatest_total
    return minimal_sum_result