from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    accumulator: int = 0
    index: int = 0
    while index < integer_k and index < len(array_of_integers):
        current_value: int = array_of_integers[index]
        if len(str(abs(current_value))) <= 2:
            accumulator += current_value
        index += 1
    return accumulator