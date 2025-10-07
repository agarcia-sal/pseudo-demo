from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    total_value: int = 0
    counter_index: int = 0
    while counter_index < integer_k and counter_index < len(array_of_integers):
        current_val: int = array_of_integers[counter_index]
        length_string: int = len(str(current_val))
        if length_string <= 2:
            total_value += current_val
        counter_index += 1
    return total_value