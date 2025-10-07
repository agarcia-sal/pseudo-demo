from typing import List

def smallest_change(input_list: List[int]) -> int:
    counter: int = 0
    position: int = 0
    half_length: int = len(input_list) // 2
    while position < half_length:
        if input_list[position] != input_list[len(input_list) - 1 - position]:
            counter += 1
        position += 1
    return counter