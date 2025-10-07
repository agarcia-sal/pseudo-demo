from typing import Iterable, List, TypeVar

T = TypeVar("T", bound=float)

def get_positive(collection_of_values: Iterable[T]) -> List[T]:
    selected_positives: List[T] = []
    cnt: int = 0
    values_list = list(collection_of_values)  # to support indexing

    while cnt < len(values_list):
        if 0 < values_list[cnt]:
            selected_positives.append(values_list[cnt])
        cnt += 1

    return selected_positives