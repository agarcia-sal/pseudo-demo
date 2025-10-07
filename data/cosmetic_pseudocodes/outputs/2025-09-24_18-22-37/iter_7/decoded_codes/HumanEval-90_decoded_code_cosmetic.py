from typing import Sequence, Optional

def next_smallest(sequence_of_numbers: Sequence[int]) -> Optional[int]:
    distinct_elements = list(dict.fromkeys(sequence_of_numbers))
    ordered_elements = sorted(distinct_elements)
    count_elements = len(ordered_elements)
    if count_elements < 2:
        return None
    return ordered_elements[1]