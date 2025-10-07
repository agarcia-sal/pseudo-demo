from typing import List

def solution(list_of_integers: List[int]) -> int:
    total_sum: int = 0
    current_position: int = 0

    while current_position < len(list_of_integers):
        element_value: int = list_of_integers[current_position]
        if current_position % 2 == 0:
            if element_value % 2 == 1:
                total_sum += element_value
        current_position += 1

    return total_sum