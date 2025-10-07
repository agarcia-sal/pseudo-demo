from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    result_string: str = ""
    current_position: int = 0
    while current_position < len(list_of_strings):
        current_string: str = list_of_strings[current_position]
        result_string += current_string
        current_position += 1
    return result_string