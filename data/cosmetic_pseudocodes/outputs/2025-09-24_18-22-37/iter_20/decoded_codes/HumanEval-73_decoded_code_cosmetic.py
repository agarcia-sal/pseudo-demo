from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    result_counter: int = 0
    total_elements: int = len(array_of_integers)
    mid_point: int = (total_elements // 2) - 1

    current_position: int = 0
    while current_position <= mid_point:
        front_element: int = array_of_integers[current_position]
        back_index: int = total_elements - current_position - 1
        back_element: int = array_of_integers[back_index]

        if front_element != back_element:
            result_counter += 1

        current_position += 1

    return result_counter