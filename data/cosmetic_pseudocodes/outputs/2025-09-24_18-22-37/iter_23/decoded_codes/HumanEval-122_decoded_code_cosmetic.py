from typing import Sequence

def add_elements(numbers_collection: Sequence[int], count_limit: int) -> int:
    accumulated_sum = 0
    iterator_index = 0
    while iterator_index < count_limit:
        current_number = numbers_collection[iterator_index]
        string_form = str(current_number)
        string_length = len(string_form)
        if string_length <= 2:
            accumulated_sum += current_number
        iterator_index += 1
    return accumulated_sum