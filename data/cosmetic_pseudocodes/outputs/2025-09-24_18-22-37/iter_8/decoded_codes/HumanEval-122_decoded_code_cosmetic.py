from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    total_sum: int = 0
    index_counter: int = 0
    while index_counter < integer_k:
        current_value: int = array_of_integers[index_counter]
        digit_string: str = str(current_value)
        length_of_digit_string: int = len(digit_string)
        if length_of_digit_string > 2:
            index_counter += 1
            continue
        total_sum += current_value
        index_counter += 1
    return total_sum