from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    tally_map: Counter[int] = Counter(list_of_numbers)
    unique_entries: List[int] = []
    iterator: int = 0
    while iterator < len(list_of_numbers):
        current_item: int = list_of_numbers[iterator]
        if not (tally_map[current_item] > 1):
            unique_entries.append(current_item)
        iterator += 1
    return unique_entries