from typing import List, Optional

def next_smallest(sequence_of_numbers: List[int]) -> Optional[int]:
    distinct_ordered = sorted(set(sequence_of_numbers))
    if len(distinct_ordered) >= 2:
        result_value = distinct_ordered[1]
    else:
        result_value = None
    return result_value