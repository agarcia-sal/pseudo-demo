from typing import Optional, Tuple, Sequence


def find_closest_elements(numbers_collection: Sequence[int]) -> Optional[Tuple[int, int]]:
    pair_closest: Optional[Tuple[int, int]] = None
    min_gap: Optional[int] = None

    length = len(numbers_collection)
    if length < 2:
        return None  # No pairs exist

    i = 0
    while i < length - 1:
        current_val = numbers_collection[i]
        j = 0
        while j < length - 1:
            candidate_val = numbers_collection[j]
            if i != j:
                diff = abs(candidate_val - current_val)
                if min_gap is None or diff < min_gap:
                    min_gap = diff
                    pair_closest = (
                        (current_val, candidate_val)
                        if current_val < candidate_val
                        else (candidate_val, current_val)
                    )
            j += 1
        i += 1

    return pair_closest