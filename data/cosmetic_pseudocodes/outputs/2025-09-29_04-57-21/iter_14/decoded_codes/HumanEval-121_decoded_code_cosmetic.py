from typing import List

def solution(list_of_integers: List[int]) -> int:
    total_result: int = 0
    position_index: int = 0
    while position_index < len(list_of_integers):
        current_item: int = list_of_integers[position_index]
        if (position_index % 2 not in {1}) and (current_item % 2 != 0):
            total_result += current_item
        position_index += 1
    return total_result