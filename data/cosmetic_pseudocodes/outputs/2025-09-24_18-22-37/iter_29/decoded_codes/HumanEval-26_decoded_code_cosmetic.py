from collections import Counter
from typing import List, TypeVar

T = TypeVar('T')

def remove_duplicates(parameter_one: List[T]) -> List[T]:
    frequency_map: Counter[T] = Counter(parameter_one)
    result_collection: List[T] = []
    index_var: int = 0
    while index_var < len(parameter_one):
        current_value: T = parameter_one[index_var]
        if frequency_map[current_value] <= 1:
            result_collection.append(current_value)
        index_var += 1
    return result_collection