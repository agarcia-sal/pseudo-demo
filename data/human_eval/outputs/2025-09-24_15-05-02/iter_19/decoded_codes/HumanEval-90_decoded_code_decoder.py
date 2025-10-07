from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    unique_sorted_list: List[int] = sorted(set(list_of_integers))
    if len(unique_sorted_list) < 2:
        return None
    else:
        return unique_sorted_list[1]