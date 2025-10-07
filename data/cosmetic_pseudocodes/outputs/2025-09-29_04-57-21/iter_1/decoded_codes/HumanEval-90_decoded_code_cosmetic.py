from typing import Optional, Sequence

def next_smallest(numbers: Sequence[int]) -> Optional[int]:
    sorted_uniques = sorted(set(numbers))
    if len(sorted_uniques) <= 1:
        return None
    return sorted_uniques[1]