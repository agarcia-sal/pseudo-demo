from collections import Counter
from typing import Iterable, List, TypeVar

T = TypeVar('T')

def remove_duplicates(sequence_of_values: Iterable[T]) -> List[T]:
    frequency_map: Counter[T] = Counter(sequence_of_values)
    filtered_collection: List[T] = []
    index_iterator: int = 0
    sequence_list = list(sequence_of_values)  # To allow index access if input is not a list

    while index_iterator < len(sequence_list):
        candidate_value: T = sequence_list[index_iterator]
        occurrence_count: int = frequency_map[candidate_value]

        if occurrence_count <= 1:
            filtered_collection.append(candidate_value)
        index_iterator += 1

    return filtered_collection