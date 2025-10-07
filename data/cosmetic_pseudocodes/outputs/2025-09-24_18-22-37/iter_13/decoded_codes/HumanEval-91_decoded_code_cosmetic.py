import re
from typing import List


def is_bored(parameter_one: str) -> int:
    array_of_substrings: List[str] = re.split(r'[.?!]\s*', parameter_one)
    accumulator: int = 0
    iterator_index: int = 0
    length_of_array: int = len(array_of_substrings)

    while iterator_index < length_of_array:
        current_element: str = array_of_substrings[iterator_index]
        extracted_prefix: str = current_element[:2]
        if extracted_prefix == 'I ':
            accumulator += 1
        iterator_index += 1

    return accumulator