from typing import List, Optional, Tuple

def find_closest_elements(array_of_values: List[int]) -> Optional[Tuple[int, int]]:
    pair_candidate: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None

    for posA, valA in enumerate(array_of_values):
        for posB, valB in enumerate(array_of_values):
            if posA != posB:
                gap_candidate = abs(valA - valB)
                if smallest_gap is None or gap_candidate < smallest_gap:
                    smallest_gap = gap_candidate
                    pair_candidate = tuple(sorted((valA, valB)))

    return pair_candidate