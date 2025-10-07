from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    sorted_unique_list = sorted(set(list_of_integers))
    if len(sorted_unique_list) < 2:
        return None
    return sorted_unique_list[1]