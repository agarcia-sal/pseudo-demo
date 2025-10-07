from typing import List, Optional

def next_smallest(input_numbers: List[int]) -> Optional[int]:
    distinct_values = sorted(set(input_numbers))
    if len(distinct_values) < 2:
        return None
    return distinct_values[1]