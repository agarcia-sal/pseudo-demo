from typing import Sequence

def add_elements(p_list: Sequence[int], p_count: int) -> int:
    total_sum: int = 0
    index_counter: int = 0
    while index_counter < p_count:
        current_value: int = p_list[index_counter]
        digit_str: str = str(current_value)
        length_str: int = len(digit_str)
        if length_str <= 2:
            total_sum += current_value
        index_counter += 1
    return total_sum