from typing import Iterable, Optional, List

def next_smallest(number_sequence: Iterable[int]) -> Optional[int]:
    distinct_values: List[int] = []
    for item in number_sequence:
        if item not in distinct_values:
            distinct_values.append(item)
    ordered_values = sorted(distinct_values)
    if len(ordered_values) < 2:
        return None
    return ordered_values[1]