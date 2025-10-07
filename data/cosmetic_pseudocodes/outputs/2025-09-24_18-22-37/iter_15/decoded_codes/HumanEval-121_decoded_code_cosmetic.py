from typing import List

def solution(array_of_values: List[int]) -> int:
    accumulator: int = 0
    position: int = 0
    length: int = len(array_of_values)
    while position < length:
        current_item: int = array_of_values[position]
        if position % 2 == 0:
            if current_item % 2 == 1:
                accumulator += current_item
        position += 1
    return accumulator