from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=float)

def get_positive(input_collection: Iterable[T]) -> List[T]:
    accumulator: List[T] = []
    iterator_index: int = 0
    input_list = list(input_collection)  # Allows indexing
    while iterator_index < len(input_list):
        candidate_element = input_list[iterator_index]
        if candidate_element > 0:
            accumulator.append(candidate_element)
        iterator_index += 1
    return accumulator