from typing import Sequence

def concatenate(strings_collection: Sequence[str]) -> str:
    result_string = ""
    iterator_index = 0
    while iterator_index < len(strings_collection):
        current_string = strings_collection[iterator_index]
        result_string += current_string
        iterator_index += 1
    return result_string