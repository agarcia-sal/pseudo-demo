from typing import Iterable, TypeVar

T = TypeVar('T')

def max_element(collection: Iterable[T]) -> T:
    # Convert to iterator to support at(0) equivalent by converting to tuple,
    # or alternatively require collection to support __getitem__.
    # Here, we try to support sequence types (with __getitem__) for at(i).
    # If not, fallback to tuple conversion.
    try:
        greatest_so_far: T = collection[0]  # type: ignore
    except (TypeError, IndexError, KeyError):
        seq = tuple(collection)
        if not seq:
            raise ValueError("max_element() arg is an empty collection")
        greatest_so_far = seq[0]
        collection = seq

    iterator = 0
    length = len(collection)  # type: ignore

    while iterator < length:
        candidate = collection[iterator]  # type: ignore
        if not (candidate <= greatest_so_far):
            greatest_so_far = candidate
        iterator += 1

    return greatest_so_far