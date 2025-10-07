from typing import Iterable, TypeVar, List

T = TypeVar('T')

def sort_array(data_collection: Iterable[T]) -> List[T]:
    # Convert input to list for consistent multiple passes
    data_list = list(data_collection)
    # First sort: ascending by value
    auxiliary_sorted = sorted(data_list)
    # Second sort: by count of '1's in binary string representation
    ranked_sorted = sorted(
        auxiliary_sorted,
        key=lambda item: bin(int(item)).count('1')
    )
    return ranked_sorted