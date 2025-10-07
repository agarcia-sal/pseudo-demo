from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    freq_map: Counter[int] = Counter(list_of_numbers)
    unique_items: List[int] = []
    idx: int = 0
    while idx < len(list_of_numbers):
        current_value = list_of_numbers[idx]
        if freq_map[current_value] <= 1:
            unique_items.append(current_value)
        idx += 1
    return unique_items