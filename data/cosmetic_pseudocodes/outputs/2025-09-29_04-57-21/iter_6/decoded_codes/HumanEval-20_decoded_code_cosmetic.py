from typing import Optional, Tuple, Sequence


def find_closest_elements(numbers_collection: Sequence[int]) -> Optional[Tuple[int, int]]:
    best_match: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None

    length = len(numbers_collection)
    for primary_pos in range(length):
        primary_value = numbers_collection[primary_pos]
        for secondary_pos in range(length):
            if primary_pos != secondary_pos:
                secondary_value = numbers_collection[secondary_pos]
                current_diff = abs(primary_value - secondary_value)
                if smallest_gap is None or current_diff < smallest_gap:
                    smallest_gap = current_diff
                    if primary_value < secondary_value:
                        best_match = (primary_value, secondary_value)
                    else:
                        best_match = (secondary_value, primary_value)
    return best_match