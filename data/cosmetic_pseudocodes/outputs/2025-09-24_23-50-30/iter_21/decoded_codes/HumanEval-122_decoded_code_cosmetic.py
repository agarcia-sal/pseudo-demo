from typing import List

def add_elements(list_of_numbers: List[int], limit: int) -> int:
    total_sum = 0
    index = 0
    while index < limit:
        current_item = list_of_numbers[index]
        if len(str(current_item)) <= 2:
            total_sum += current_item
        index += 1
    return total_sum