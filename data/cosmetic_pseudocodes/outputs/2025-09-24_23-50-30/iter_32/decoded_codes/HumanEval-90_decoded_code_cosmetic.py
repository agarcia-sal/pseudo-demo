from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    temp_array = sorted(set(list_of_integers))
    if len(temp_array) < 2:
        return None
    else:
        return temp_array[1]