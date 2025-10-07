from typing import Sequence, Optional, Tuple, TypeVar

T = TypeVar('T', bound=float)  # Assuming elements support float operations and comparisons

def find_closest_elements(collection: Sequence[T]) -> Optional[Tuple[T, T]]:
    result_pair: Optional[Tuple[T, T]] = None
    smallest_gap: Optional[float] = None
    outer_idx = 0
    length = len(collection)

    while outer_idx < length:
        outer_val = collection[outer_idx]
        inner_idx = 0

        while inner_idx < length:
            if outer_idx == inner_idx:
                inner_idx += 1
                continue

            inner_val = collection[inner_idx]
            diff_abs = abs(outer_val - inner_val)

            if smallest_gap is None:
                smallest_gap = diff_abs
                result_pair = (outer_val, inner_val) if outer_val < inner_val else (inner_val, outer_val)
            else:
                if diff_abs < smallest_gap:
                    smallest_gap = diff_abs
                    result_pair = (outer_val, inner_val)
                    if result_pair[0] > result_pair[1]:
                        result_pair = (result_pair[1], result_pair[0])

            inner_idx += 1
        outer_idx += 1

    return result_pair