from typing import List

def add_elements(array_of_integers: List[int], limit: int) -> int:
    sum_of_elements = 0
    max_index = min(limit, len(array_of_integers))
    for index in range(max_index):
        current_element = array_of_integers[index]
        element_length = len(str(current_element))
        if element_length <= 2:
            sum_of_elements += current_element
    return sum_of_elements