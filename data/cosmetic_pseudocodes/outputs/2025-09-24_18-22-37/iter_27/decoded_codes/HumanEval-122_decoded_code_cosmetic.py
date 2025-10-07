from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    accumulated_total: int = 0
    iteration_counter: int = 0
    while iteration_counter < integer_k:
        current_entry: int = array_of_integers[iteration_counter]
        string_version: str = str(current_entry)
        string_length: int = len(string_version)
        if string_length <= 2:
            accumulated_total += current_entry
        iteration_counter += 1
    return accumulated_total