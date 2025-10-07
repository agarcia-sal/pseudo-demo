from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    filtered_items: List[int] = []
    for val in list_of_integers:
        if val not in filtered_items:
            filtered_items.append(val)
    sorted_unique = filtered_items
    sorted_unique.sort()
    if len(sorted_unique) < 2:
        return None
    else:
        return sorted_unique[1]