from typing import List, Sequence, TypeVar

T = TypeVar('T', bound=float)

def get_positive(numeric_collection: Sequence[T]) -> List[T]:
    result_container: List[T] = []
    idx = 0
    while idx < len(numeric_collection):
        if not (numeric_collection[idx] <= 0):
            result_container.append(numeric_collection[idx])
        idx += 1
    return result_container