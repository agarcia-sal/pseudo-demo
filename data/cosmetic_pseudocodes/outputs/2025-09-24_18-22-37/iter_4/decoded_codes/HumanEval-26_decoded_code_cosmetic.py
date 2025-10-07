from collections import Counter
from typing import List, TypeVar

T = TypeVar('T')

def remove_duplicates(input_array: List[T]) -> List[T]:
    occurrence_map = Counter(input_array)
    filtered_result: List[T] = []
    index = 0
    while index < len(input_array):
        current_item = input_array[index]
        if occurrence_map[current_item] <= 1:
            filtered_result.append(current_item)
        index += 1
    return filtered_result