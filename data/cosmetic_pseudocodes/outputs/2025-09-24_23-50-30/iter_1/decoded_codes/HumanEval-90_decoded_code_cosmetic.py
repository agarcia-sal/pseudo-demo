from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    temp_set: set[int] = set()
    for number in list_of_integers:
        temp_set.add(number)
    unique_sorted_list: List[int] = sorted(temp_set)
    if len(unique_sorted_list) >= 2:
        return unique_sorted_list[1]
    return None