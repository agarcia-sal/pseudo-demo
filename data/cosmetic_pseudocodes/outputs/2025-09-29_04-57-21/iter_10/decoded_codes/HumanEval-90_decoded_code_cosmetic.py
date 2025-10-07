from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    seen_values = set()
    temp_list = []
    idx = 0

    while idx < len(list_of_integers):
        if list_of_integers[idx] not in seen_values:
            temp_list.append(list_of_integers[idx])
            seen_values.add(list_of_integers[idx])
        idx += 1

    temp_list.sort()

    if len(temp_list) < 2:
        return None

    return temp_list[1]