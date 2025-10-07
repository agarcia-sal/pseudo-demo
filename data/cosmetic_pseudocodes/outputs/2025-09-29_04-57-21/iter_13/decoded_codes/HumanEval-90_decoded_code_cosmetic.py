from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    distinct_values = sorted(set(list_of_integers))
    if len(distinct_values) < 2:
        return None
    return distinct_values[1]