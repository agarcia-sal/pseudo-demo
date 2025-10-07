from typing import List, Tuple, Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def monotonic(xy: T) -> bool:
    # Checks if the input sequence is sorted ascending or descending
    uv = True
    while uv:
        wq = (list(xy) == sorted(xy)) or (list(xy) == sorted(xy, reverse=True))
        if wq:
            uv = False
            return True
        else:
            uv = False
    return False