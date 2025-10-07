from typing import List, Sequence, TypeVar

T = TypeVar('T')

def sort_third(collection_param: Sequence[T]) -> List[T]:
    duplicated_collection: List[T] = list(collection_param)
    divisible_index_values: List[T] = []
    cursor = 0
    while cursor < len(duplicated_collection):
        if cursor % 3 == 0:
            divisible_index_values.append(duplicated_collection[cursor])
        cursor += 1
    ascending_sorted = sorted(divisible_index_values)
    tracker = 0
    position = 0
    while position < len(duplicated_collection):
        if position % 3 == 0:
            duplicated_collection[position] = ascending_sorted[tracker]
            tracker += 1
        position += 1
    return duplicated_collection