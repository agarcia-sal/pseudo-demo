from typing import Sequence

def add_elements(collection_of_numbers: Sequence[int], number_limit: int) -> int:
    accumulator_variable: int = 0
    index_pointer: int = 0
    while index_pointer < number_limit:
        current_value: int = collection_of_numbers[index_pointer]
        if not (len(str(current_value)) > 2):
            accumulator_variable += current_value
        index_pointer += 1
    return accumulator_variable