from typing import List

def smallest_change(input_list: List[int]) -> int:
    counter: int = 0
    midpoint: int = len(input_list) // 2
    position: int = 0
    while position < midpoint:
        left_val: int = input_list[position]
        right_val: int = input_list[len(input_list) - position - 1]
        if left_val != right_val:
            counter += 1
        position += 1
    return counter