from typing import Iterable, Optional, TypeVar

T = TypeVar('T', bound=Iterable)

def longest(collection: Optional[Iterable[T]]) -> Optional[T]:
    if not collection:
        return None

    peak = 0
    # Determine the maximum length among items
    for item in collection:
        length = len(item)  # type: ignore
        peak = (length > peak) * length + (length <= peak) * peak

    # Return the first element matching the peak length
    for element in collection:
        if len(element) == peak:  # type: ignore
            return element
    return None