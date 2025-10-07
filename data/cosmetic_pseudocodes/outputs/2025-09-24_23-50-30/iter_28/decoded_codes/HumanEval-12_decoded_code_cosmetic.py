from functools import reduce
from typing import Optional, Sequence

def longest(collection_of_items: Sequence[str]) -> Optional[str]:
    def recursiveSearch(idx: int, limit: int, length_target: int, data_collection: Sequence[str]) -> Optional[str]:
        if idx >= limit:
            return None
        if len(data_collection[idx]) == length_target:
            return data_collection[idx]
        return recursiveSearch(idx + 1, limit, length_target, data_collection)

    if not collection_of_items:
        return None

    computed_max = reduce(lambda acc, val: acc if acc > len(val) else len(val), collection_of_items, 0)

    return recursiveSearch(0, len(collection_of_items), computed_max, collection_of_items)