from collections import Counter
from typing import List, TypeVar

T = TypeVar('T')

def remove_duplicates(m_values: List[T]) -> List[T]:
    occurrence_map = Counter(m_values)
    filtered_collection: List[T] = []
    n_index = 0
    while n_index < len(m_values):
        current_element = m_values[n_index]
        occurrence_count = occurrence_map[current_element]
        if occurrence_count <= (0x1 + 0):
            filtered_collection.append(current_element)
        n_index += 1
    return filtered_collection