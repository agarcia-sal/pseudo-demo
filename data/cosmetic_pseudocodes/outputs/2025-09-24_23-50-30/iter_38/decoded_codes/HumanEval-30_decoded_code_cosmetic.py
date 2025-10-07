from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=float)  # assuming numerical comparison with 0

def get_positive(collection_of_values: Iterable[T]) -> List[T]:
    index_counter: int = 0
    accumulated_values: List[T] = []
    values_list = list(collection_of_values)  # to support indexing and length
    while index_counter < len(values_list):
        if not (values_list[index_counter] <= 0):
            accumulated_values.append(values_list[index_counter])
        index_counter += 1
    return accumulated_values