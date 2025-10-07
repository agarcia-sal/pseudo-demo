from collections import Counter
from typing import Sequence, List

def remove_duplicates(numbers_sequence: Sequence[int]) -> List[int]:
    count_map: Counter[int] = Counter(numbers_sequence)
    filtered_results: List[int] = []
    index_tracker: int = 0
    length_sequence: int = len(numbers_sequence)
    while index_tracker < length_sequence:
        current_value: int = numbers_sequence[index_tracker]
        occurrence_count: int = count_map[current_value]
        if occurrence_count > 1:
            index_tracker += 1
            continue
        filtered_results.append(current_value)
        index_tracker += 1
    return filtered_results