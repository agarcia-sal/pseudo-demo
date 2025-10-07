from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    distinct_numbers = sorted(set(list_of_integers))
    if len(distinct_numbers) < 2:
        return None
    return distinct_numbers[1]