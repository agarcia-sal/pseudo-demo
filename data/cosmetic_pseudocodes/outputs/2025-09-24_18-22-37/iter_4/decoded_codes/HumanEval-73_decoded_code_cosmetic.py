from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    count_diff: int = 0
    length_val: int = len(array_of_integers)
    midpoint: int = length_val // 2
    iterator: int = 0
    while iterator < midpoint:
        front_element: int = array_of_integers[iterator]
        rear_element: int = array_of_integers[length_val - iterator - 1]
        if front_element != rear_element:
            count_diff += 1
        iterator += 1
    return count_diff