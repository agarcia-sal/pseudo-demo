from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    accumulated_string: str = ""
    current_position: int = 0
    total_elements: int = len(list_of_strings)
    while current_position < total_elements:
        accumulated_string += list_of_strings[current_position]
        current_position += 1
    return accumulated_string