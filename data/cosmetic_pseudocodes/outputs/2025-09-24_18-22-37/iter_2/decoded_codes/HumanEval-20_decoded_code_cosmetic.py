from typing import List, Optional, Tuple

def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    best_match: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None

    for pos_a, val_a in enumerate(list_of_numbers):
        for pos_b, val_b in enumerate(list_of_numbers):
            if pos_a != pos_b:
                current_gap = abs(val_a - val_b)
                if smallest_gap is None or current_gap < smallest_gap:
                    smallest_gap = current_gap
                    best_match = tuple(sorted((val_a, val_b)))

    return best_match