from typing import Optional, Sequence, Sized, TypeVar

T = TypeVar('T', bound=Sized)

def longest(collection: Sequence[T]) -> Optional[T]:
    if not collection:
        return None
    maxLen = 0
    for element in collection:
        if len(element) > maxLen:
            maxLen = len(element)
    for candidate in collection:
        if len(candidate) == maxLen:
            return candidate
    return None  # fallback, though logically unreachable