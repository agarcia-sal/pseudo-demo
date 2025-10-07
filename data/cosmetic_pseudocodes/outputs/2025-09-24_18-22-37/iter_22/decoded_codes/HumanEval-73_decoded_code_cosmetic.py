from typing import Sequence

def smallest_change(values: Sequence[int]) -> int:
    result: int = 0
    half_length: int = len(values) // 2
    position: int = 0
    while position < half_length:
        left_element = values[position]
        right_index = len(values) - position - 1
        right_element = values[right_index]
        if left_element != right_element:
            result += 1
        position += 1
    return result