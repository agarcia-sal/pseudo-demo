from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=float)  # Assuming elements are numbers supporting comparison with 0

def get_positive(sequence: Iterable[T]) -> List[T]:
    result_collection: List[T] = []
    iterator = iter(sequence)

    while True:
        try:
            current_item = next(iterator)
        except StopIteration:
            break
        if not (current_item <= 0):
            result_collection.append(current_item)

    return result_collection