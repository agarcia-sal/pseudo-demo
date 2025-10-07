from typing import Iterable, Optional

def next_smallest(collection_of_numbers: Iterable[int]) -> Optional[int]:
    distinct_ordered = sorted(set(collection_of_numbers))
    if len(distinct_ordered) < 2:
        return None
    return distinct_ordered[1]