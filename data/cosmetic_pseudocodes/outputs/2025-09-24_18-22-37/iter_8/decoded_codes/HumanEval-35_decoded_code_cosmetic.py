from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(collection: Sequence[T]) -> T:
    leader_candidate: T = collection[0]
    iterator_index: int = 0
    while iterator_index < len(collection):
        current_value: T = collection[iterator_index]
        if current_value > leader_candidate:
            leader_candidate = current_value
        iterator_index += 1
    return leader_candidate