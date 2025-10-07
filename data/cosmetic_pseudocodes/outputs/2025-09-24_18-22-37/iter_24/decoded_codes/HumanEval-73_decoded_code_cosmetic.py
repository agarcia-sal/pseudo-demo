from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    counter: int = 0
    position: int = 0
    boundary: int = len(array_of_integers) // 2
    limit: int = boundary - 1
    while position <= limit:
        left_element: int = array_of_integers[position]
        right_index: int = len(array_of_integers) - position - 1
        right_element: int = array_of_integers[right_index]
        if left_element != right_element:
            counter += 1
        position += 1
    return counter