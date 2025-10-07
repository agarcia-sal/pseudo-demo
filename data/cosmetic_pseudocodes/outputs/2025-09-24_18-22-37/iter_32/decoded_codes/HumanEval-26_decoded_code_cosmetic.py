from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    frequency_map: Counter[int] = Counter(list_of_numbers)
    filtered_list: List[int] = []
    idx: int = 0

    while idx < len(list_of_numbers):
        current_value: int = list_of_numbers[idx]
        if frequency_map[current_value] <= 1:
            filtered_list.append(current_value)
        idx += 1

    return filtered_list