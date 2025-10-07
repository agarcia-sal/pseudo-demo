from typing import List, Optional, Union

def pluck(collection_of_items: List[int]) -> List[Union[int, int]]:
    def find_min_even(
        coll: List[int], current_min: Optional[int] = None
    ) -> Optional[int]:
        if not coll:
            return current_min
        candidate, rest = coll[0], coll[1:]
        if candidate % 2 == 0:
            new_min = candidate if current_min is None or candidate < current_min else current_min
        else:
            new_min = current_min
        return find_min_even(rest, new_min)

    minimal_even = find_min_even(collection_of_items)
    if minimal_even is None:
        return []

    position = 0
    length = len(collection_of_items)
    while position < length and collection_of_items[position] != minimal_even:
        position += 1

    return [minimal_even, position]