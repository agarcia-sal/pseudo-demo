from collections import Counter
from typing import List

def remove_duplicates(number_sequence: List[int]) -> List[int]:
    frequency_map: Counter[int] = Counter(number_sequence)
    filtered_result: List[int] = []
    index: int = 0
    while index < len(number_sequence):
        current_element = number_sequence[index]
        occurrence_count = frequency_map[current_element]
        if occurrence_count > 1:
            pass  # skip elements with duplicates
        else:
            filtered_result.append(current_element)
        index += 1
    return filtered_result