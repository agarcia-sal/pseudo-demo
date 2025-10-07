from collections import Counter
from typing import List, TypeVar

T = TypeVar('T')

def remove_duplicates(array_of_values: List[T]) -> List[T]:
    frequency_dictionary: Counter[T] = Counter(array_of_values)
    result_collection: List[T] = []
    index_tracker: int = 0
    while index_tracker < len(array_of_values):
        if not (frequency_dictionary[array_of_values[index_tracker]] > 1):
            result_collection.append(array_of_values[index_tracker])
        index_tracker += 1
    return result_collection