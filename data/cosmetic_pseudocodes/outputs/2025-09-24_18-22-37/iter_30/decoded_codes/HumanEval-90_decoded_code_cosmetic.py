from typing import List, Optional

def next_smallest(array_of_nums: List[int]) -> Optional[int]:
    distinct_ordered_values = sorted(set(array_of_nums))
    count_unique = len(distinct_ordered_values)
    if count_unique < 2:
        return None
    outcome: int = distinct_ordered_values[1]
    return outcome