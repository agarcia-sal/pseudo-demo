from typing import Sequence, Optional

def next_smallest(sequence_of_numbers: Sequence[int]) -> Optional[int]:
    distinct_ordered_collection = sorted(set(sequence_of_numbers))
    if len(distinct_ordered_collection) < 2:
        return None
    return distinct_ordered_collection[1]