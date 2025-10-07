from typing import List

def add_elements(list_numbers: List[int], count_limit: int) -> int:
    total_value: int = 0
    index_tracker: int = 0
    while index_tracker < count_limit:
        current_value: int = list_numbers[index_tracker]
        if len(str(current_value)) > 2:
            break
        else:
            total_value += current_value
        index_tracker += 1
    return total_value