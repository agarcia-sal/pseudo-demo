from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    frequency_map: Counter[int] = Counter(list_of_numbers)
    unique_items: List[int] = []
    for number in list_of_numbers:
        if frequency_map[number] <= 1:
            unique_items.append(number)
    return unique_items