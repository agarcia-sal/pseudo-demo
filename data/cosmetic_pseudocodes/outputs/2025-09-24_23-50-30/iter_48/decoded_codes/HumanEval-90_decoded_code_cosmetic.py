from typing import Sequence, Optional, TypeVar, List

T = TypeVar('T')


def next_smallest(sequence: Sequence[T]) -> Optional[T]:
    temp_collection: List[T] = []
    for element in sequence:
        if element not in temp_collection:
            temp_collection.append(element)

    sorted_collection: List[T] = []
    while len(temp_collection) > 0:
        min_val = temp_collection[0]
        index = 0
        idx_counter = 1
        while idx_counter < len(temp_collection):
            if not (temp_collection[idx_counter] >= min_val):
                min_val = temp_collection[idx_counter]
                index = idx_counter
            idx_counter += 1
        sorted_collection.append(min_val)
        temp_collection.pop(index)

    if len(sorted_collection) < 2:
        return None
    else:
        return sorted_collection[1]