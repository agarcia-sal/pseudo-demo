from typing import Sequence

def add(array_parameter: Sequence[int]) -> int:
    total_accumulator: int = 0
    current_idx: int = 1
    while current_idx <= len(array_parameter):
        current_element: int = array_parameter[current_idx - 1]  # 1-based to 0-based index
        if current_element % 2 == 0:
            total_accumulator += current_element
        current_idx += 2
    return total_accumulator