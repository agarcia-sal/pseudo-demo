from typing import Sequence

def add_elements(collection_of_numbers: Sequence[int], limit_value: int) -> int:
    accumulator_var = 0
    counter_var = 0
    while counter_var < limit_value:
        current_item = collection_of_numbers[counter_var]
        if not (len(str(current_item)) > 2):
            accumulator_var += current_item
        counter_var += 1
    return accumulator_var