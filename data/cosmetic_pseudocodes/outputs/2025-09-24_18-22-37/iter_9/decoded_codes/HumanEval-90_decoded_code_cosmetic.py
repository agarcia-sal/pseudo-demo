from typing import Iterable, Optional

def next_smallest(sequence_of_numbers: Iterable[int]) -> Optional[int]:
    filtered_collection = sorted(set(sequence_of_numbers))
    if len(filtered_collection) < 2:
        return None
    return filtered_collection[1]