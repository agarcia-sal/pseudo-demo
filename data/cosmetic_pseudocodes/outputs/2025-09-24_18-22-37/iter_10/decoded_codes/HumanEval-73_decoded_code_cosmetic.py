from typing import List


def smallest_change(array_of_integers: List[int]) -> int:
    deviation_counter: int = 0
    boundary_limit: int = len(array_of_integers) // 2
    position_cursor: int = 0
    while position_cursor < boundary_limit:
        left_element: int = array_of_integers[position_cursor]
        right_index: int = len(array_of_integers) - position_cursor - 1
        right_element: int = array_of_integers[right_index]
        if left_element != right_element:
            deviation_counter += 1
        position_cursor += 1
    return deviation_counter