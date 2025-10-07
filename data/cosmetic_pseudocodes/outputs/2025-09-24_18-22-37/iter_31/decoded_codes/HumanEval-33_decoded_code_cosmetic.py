from typing import Iterable, List, TypeVar

T = TypeVar('T')

def sort_third(collection_param: Iterable[T]) -> List[T]:
    working_collection: List[T] = list(collection_param)
    selected_elements: List[T] = [working_collection[i] for i in range(len(working_collection)) if i % 3 == 0]
    ordered_elements: List[T] = sorted(selected_elements)
    iterator_index: int = 0
    for position in range(len(working_collection)):
        if position % 3 == 0:
            working_collection[position] = ordered_elements[iterator_index]
            iterator_index += 1
    return working_collection