from typing import Iterable, List

def incr_list(collection_of_items: Iterable[int]) -> List[int]:
    augmented_collection: List[int] = []
    for item in collection_of_items:
        incremented_item = item + 1
        augmented_collection.append(incremented_item)
    return augmented_collection