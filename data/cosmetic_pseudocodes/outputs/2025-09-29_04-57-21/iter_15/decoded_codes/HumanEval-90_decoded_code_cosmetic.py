from typing import List, Optional

def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    filtered_collection: List[int] = []
    for number in list_of_integers:
        if number not in filtered_collection:
            filtered_collection.append(number)
    ordered_collection = sorted(filtered_collection)
    if len(ordered_collection) >= 2:
        return ordered_collection[1]
    return None