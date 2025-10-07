from collections import Counter
from typing import Sequence, List

def remove_duplicates(numbers_sequence: Sequence[int]) -> List[int]:
    frequency_map: Counter[int] = Counter(numbers_sequence)
    unique_items_list: List[int] = []
    iterator_index = 0
    while iterator_index < len(numbers_sequence):
        current_candidate = numbers_sequence[iterator_index]
        if frequency_map[current_candidate] <= 1:
            unique_items_list.append(current_candidate)
        iterator_index += 1
    return unique_items_list