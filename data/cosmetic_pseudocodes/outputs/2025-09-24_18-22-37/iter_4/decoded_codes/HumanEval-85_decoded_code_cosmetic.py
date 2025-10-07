from typing import List

def add(input_list: List[int]) -> int:
    total_sum: int = 0
    index: int = 1
    while index <= len(input_list):
        current_element = input_list[index - 1]  # adjust for 0-based indexing
        if current_element % 2 == 0:
            total_sum += current_element
        index += 2
    return total_sum