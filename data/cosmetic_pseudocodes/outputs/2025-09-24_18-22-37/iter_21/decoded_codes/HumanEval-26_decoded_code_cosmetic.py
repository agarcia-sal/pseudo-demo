from collections import Counter
from typing import List

def remove_duplicates(numbers_collection: List[int]) -> List[int]:
    frequency_map: Counter[int] = Counter(numbers_collection)
    result_list: List[int] = []
    idx: int = 0
    length_col: int = len(numbers_collection)
    while idx < length_col:
        current_val: int = numbers_collection[idx]
        if frequency_map[current_val] <= 1:
            result_list.append(current_val)
        idx += 1
    return result_list