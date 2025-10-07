from collections import Counter
from typing import List

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    def filter_uniq(original_list: List[int], freq_map: Counter[int], idx: int) -> List[int]:
        if idx >= len(original_list):
            return []
        current_element = original_list[idx]
        if freq_map[current_element] <= 1:
            return [current_element] + filter_uniq(original_list, freq_map, idx + 1)
        return filter_uniq(original_list, freq_map, idx + 1)

    frequency_counter = Counter(list_of_numbers)
    return filter_uniq(list_of_numbers, frequency_counter, 0)