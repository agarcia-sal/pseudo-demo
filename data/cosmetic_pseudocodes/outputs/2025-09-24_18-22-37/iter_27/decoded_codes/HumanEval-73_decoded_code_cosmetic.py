from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    result_counter: int = 0
    limit: int = (len(array_of_integers) // 2) - 1
    current_pos: int = 0
    while current_pos <= limit:
        front_element: int = array_of_integers[current_pos]
        back_index: int = len(array_of_integers) - current_pos - 1
        back_element: int = array_of_integers[back_index]
        if front_element != back_element:
            result_counter += 1
        current_pos += 1
    return result_counter