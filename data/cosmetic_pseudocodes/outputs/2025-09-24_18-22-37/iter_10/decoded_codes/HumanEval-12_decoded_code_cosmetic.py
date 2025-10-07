from typing import List, Optional, Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def longest(components: Sequence[T]) -> Optional[T]:
    if components:
        tally: int = 0
        for component_var in components:
            check_len = len(component_var)
            if check_len > tally:
                tally = check_len

        for candidate in components:
            if len(candidate) == tally:
                return candidate
    return None