from typing import List, TypeVar

T = TypeVar('T')

def sort_third(array_origin: List[T]) -> List[T]:
    array_clone: List[T] = list(array_origin)
    filtered_elements: List[T] = [array_clone[idx] for idx in range(len(array_clone)) if idx % 3 == 0]
    ordered_subset: List[T] = sorted(filtered_elements)
    position_tracker: int = 0
    for i in range(len(array_clone)):
        if i % 3 == 0:
            array_clone[i] = ordered_subset[position_tracker]
            position_tracker += 1
    return array_clone