from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=object)

def unique(sequence_param: Iterable[T]) -> List[T]:
    temp_store: set[T] = set()
    for element_var in sequence_param:
        temp_store.add(element_var)
    result_sequence: List[T] = []
    for item_var in temp_store:
        result_sequence.append(item_var)
    return sorted(result_sequence)