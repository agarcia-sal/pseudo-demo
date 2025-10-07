from typing import Sequence


def add_elements(sequence_of_values: Sequence[int], quantity_limit: int) -> int:
    accumulator: int = 0
    index_counter: int = 0

    while index_counter < quantity_limit:
        current_item: int = sequence_of_values[index_counter]
        if not (len(str(current_item)) > 2):
            accumulator += current_item
        index_counter += 1

    return accumulator