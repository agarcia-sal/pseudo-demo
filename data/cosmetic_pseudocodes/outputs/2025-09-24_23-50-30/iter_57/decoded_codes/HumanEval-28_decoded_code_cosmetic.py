from typing import Sequence

def concatenate(array_of_elements: Sequence[str]) -> str:
    result_string: str = ""
    iterator_index: int = 0
    while iterator_index < len(array_of_elements):
        result_string += array_of_elements[iterator_index]
        iterator_index += 1
    return result_string