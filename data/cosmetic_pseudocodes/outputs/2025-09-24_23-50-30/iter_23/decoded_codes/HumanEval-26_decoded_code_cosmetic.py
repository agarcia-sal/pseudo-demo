from typing import Sequence, TypeVar, List, Dict

T = TypeVar('T')

def remove_duplicates(sequence_of_values: Sequence[T]) -> List[T]:
    frequency_map: Dict[T, int] = {}
    for item in sequence_of_values:
        frequency_map[item] = frequency_map.get(item, 0) + 1

    filtered_collection: List[T] = [candidate for candidate in sequence_of_values if frequency_map[candidate] == 1]
    return filtered_collection