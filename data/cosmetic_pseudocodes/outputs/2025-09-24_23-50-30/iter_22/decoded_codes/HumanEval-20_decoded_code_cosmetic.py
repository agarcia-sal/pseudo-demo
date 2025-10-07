from typing import Sequence, Optional, Tuple

def find_closest_elements(sequence_of_values: Sequence[int]) -> Optional[Tuple[int, int]]:
    pair_nearest: Optional[Tuple[int, int]] = None
    distance_minimal: Optional[int] = None
    length_seq = len(sequence_of_values)
    pointer_a = 0

    while pointer_a < length_seq - 1:
        pointer_b = pointer_a + 1
        while pointer_b < length_seq:
            value_a = sequence_of_values[pointer_a]
            value_b = sequence_of_values[pointer_b]
            gap = value_b - value_a
            gap_abs = gap if gap >= 0 else -gap

            if distance_minimal is None or gap_abs < distance_minimal:
                distance_minimal = gap_abs
                pair_nearest = (value_a, value_b) if value_a < value_b else (value_b, value_a)

            pointer_b += 1
        pointer_a += 1

    return pair_nearest