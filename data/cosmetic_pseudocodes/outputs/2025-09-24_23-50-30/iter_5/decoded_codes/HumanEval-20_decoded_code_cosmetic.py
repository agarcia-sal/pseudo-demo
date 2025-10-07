from typing import Sequence, Optional, Tuple, TypeVar

T = TypeVar('T', bound=float)  # assuming numeric comparable elements, float covers int as well

def find_closest_elements(sequence: Sequence[T]) -> Optional[Tuple[T, T]]:
    min_diff: float = float('inf')
    closest_pair: Optional[Tuple[T, T]] = None

    length = len(sequence)
    for i in range(length - 1):
        el = sequence[i]
        for j in range(i + 1, length):
            er = sequence[j]
            dist = abs(er - el)
            if dist < min_diff:
                min_diff = dist
                if el < er:
                    closest_pair = (el, er)
                else:
                    closest_pair = (er, el)

    return closest_pair