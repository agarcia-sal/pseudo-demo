from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=float)  # Assuming values are numeric (floats); can be int or float

def get_positive(sequence_of_values: Iterable[T]) -> List[T]:
    result_collection: List[T] = []
    idx: int = 0
    seq = list(sequence_of_values)  # Convert to list to allow indexing and length
    while idx < len(seq):
        if not (seq[idx] <= 0):
            result_collection.append(seq[idx])
        idx += 1
    return result_collection