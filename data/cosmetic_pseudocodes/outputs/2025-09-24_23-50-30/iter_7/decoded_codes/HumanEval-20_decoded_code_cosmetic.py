from typing import Sequence, Optional, Tuple

def find_closest_elements(sequence_numbers: Sequence[int]) -> Optional[Tuple[int, int]]:
    minimal_gap: Optional[int] = None
    pair_closest: Optional[Tuple[int, int]] = None

    for posA, valA in enumerate(sequence_numbers):
        for posB, valB in enumerate(sequence_numbers):
            if posA != posB:
                current_gap = abs(valA - valB)
                if minimal_gap is None or current_gap < minimal_gap:
                    minimal_gap = current_gap
                    pair_closest = (valA, valB)
                    if pair_closest[1] < pair_closest[0]:
                        pair_closest = (pair_closest[1], pair_closest[0])
    return pair_closest