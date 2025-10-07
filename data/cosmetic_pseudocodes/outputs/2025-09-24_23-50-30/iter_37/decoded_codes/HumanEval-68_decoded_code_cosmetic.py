from typing import List, Optional

def pluck(collection_of_items: List[int]) -> List[int]:
    if not collection_of_items:
        return []
    filtered_evens = [item for item in collection_of_items if item % 2 == 0]
    if not filtered_evens:
        return []
    minimal_even = filtered_evens[0]
    for item in filtered_evens[1:]:
        if item < minimal_even:
            minimal_even = item
    for pos, val in enumerate(collection_of_items):
        if val == minimal_even:
            return [minimal_even, pos]
    return []