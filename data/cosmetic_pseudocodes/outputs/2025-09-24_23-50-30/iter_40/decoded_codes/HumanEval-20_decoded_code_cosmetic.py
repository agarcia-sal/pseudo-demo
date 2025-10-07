from typing import Optional, Sequence, Tuple, TypeVar

T = TypeVar('T', bound=float)

def find_closest_elements(collection: Sequence[T]) -> Optional[Tuple[T, T]]:
    result_pair: Optional[Tuple[T, T]] = None
    smallest_gap: Optional[T] = None

    for posA, valA in enumerate(collection):
        for posB, valB in enumerate(collection):
            if posA != posB:
                diff = abs(valA - valB)
                if smallest_gap is None:
                    smallest_gap = diff
                    result_pair = tuple(sorted((valA, valB)))
                else:
                    if diff < smallest_gap:
                        smallest_gap = diff
                        result_pair = tuple(sorted((valA, valB)))

    return result_pair