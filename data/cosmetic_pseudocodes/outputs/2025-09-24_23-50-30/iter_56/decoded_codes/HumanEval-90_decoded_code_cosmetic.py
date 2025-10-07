from typing import List, Optional

def next_smallest(array_numbers: List[int]) -> Optional[int]:
    temp_collection = set(array_numbers)
    ordered_collection = list(temp_collection)
    ordered_collection.sort()
    if len(ordered_collection) < 2:
        return None
    else:
        return ordered_collection[1]