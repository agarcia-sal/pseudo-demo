from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    unique_sorted = sorted(set(list_of_integers))
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]