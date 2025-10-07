from typing import List

def add_elements(list_integers: List[int], count_limit: int) -> int:
    accumulator: int = 0
    index_counter: int = 0
    while index_counter < count_limit:
        current_number = list_integers[index_counter]
        str_form = str(current_number)
        if len(str_form) <= 2:
            accumulator += current_number
        index_counter += 1
    return accumulator