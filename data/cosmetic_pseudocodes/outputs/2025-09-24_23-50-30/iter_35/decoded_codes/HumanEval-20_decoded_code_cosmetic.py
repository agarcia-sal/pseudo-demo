from typing import Sequence, Optional, Tuple, TypeVar

T = TypeVar('T', bound='SupportsFloat')

class SupportsFloat:
    def __float__(self) -> float:
        ...

def find_closest_elements(input_sequence: Sequence[T]) -> Optional[Tuple[T, T]]:
    paired_values: Optional[Tuple[T, T]] = None
    smallest_gap: Optional[float] = None

    length = len(input_sequence)
    for idx_a in range(length):
        val_a = input_sequence[idx_a]
        for idx_b in range(length):
            if idx_a == idx_b:
                continue

            val_b = input_sequence[idx_b]
            # Calculate absolute difference using float conversion for general numeric types
            candidate_gap = abs(float(val_a) - float(val_b))

            if smallest_gap is None or candidate_gap < smallest_gap:
                smallest_gap = candidate_gap
                # Store the pair in ascending order
                paired_values = (val_a, val_b) if val_a < val_b else (val_b, val_a)

    return paired_values