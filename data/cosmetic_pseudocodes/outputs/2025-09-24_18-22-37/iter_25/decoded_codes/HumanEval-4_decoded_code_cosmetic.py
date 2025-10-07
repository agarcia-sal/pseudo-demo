from typing import Sequence


def mean_absolute_deviation(sequence_of_values: Sequence[float]) -> float:
    combined_sum: float = 0
    item_counter: int = 0

    while item_counter < len(sequence_of_values):
        combined_sum += sequence_of_values[item_counter]
        item_counter += 1

    count_items: int = item_counter
    average_value: float = combined_sum / count_items

    deviation_accumulator: float = 0
    index_pointer: int = 0

    while True:
        if not (index_pointer < count_items):
            break

        current_value: float = sequence_of_values[index_pointer]
        absolute_difference: float = current_value - average_value

        if absolute_difference < 0:
            absolute_difference = -absolute_difference

        deviation_accumulator += absolute_difference
        index_pointer += 1

    mad_result: float = deviation_accumulator / count_items

    return mad_result