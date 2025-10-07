from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    distinct_sequence = sorted(set(list_of_integers))
    if len(distinct_sequence) < 2:
        return None
    return distinct_sequence[1]