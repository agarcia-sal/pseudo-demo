from typing import List, TypeVar

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    seen_elements: set[T] = set()
    result_sequence: List[T] = []
    iterator_position: int = 0

    while iterator_position < len(list_of_elements):
        candidate_item = list_of_elements[iterator_position]
        if candidate_item not in seen_elements:
            result_sequence.append(candidate_item)
            seen_elements.add(candidate_item)
        iterator_position += 1

    result_sequence.sort()
    return result_sequence