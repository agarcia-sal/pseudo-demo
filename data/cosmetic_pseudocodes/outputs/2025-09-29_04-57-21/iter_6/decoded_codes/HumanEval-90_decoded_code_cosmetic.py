from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    distinct_values: List[int] = []
    for element in list_of_integers:
        if element not in distinct_values:
            distinct_values.append(element)
    distinct_values.sort()
    if len(distinct_values) <= 1:
        return None
    return distinct_values[1]