from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=float)

def get_positive(input_collection: Iterable[T]) -> List[T]:
    return [candidate_element for candidate_element in input_collection if candidate_element > 0]