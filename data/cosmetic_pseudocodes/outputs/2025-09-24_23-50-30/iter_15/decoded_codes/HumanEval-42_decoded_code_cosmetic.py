from typing import Sequence, List

def incr_list(set_of_items: Sequence[int]) -> List[int]:
    updated_collection: List[int] = []
    index_counter: int = 0

    while index_counter < len(set_of_items):
        current_item: int = set_of_items[index_counter]
        incremented_item: int = current_item - (-1)  # equivalent to current_item + 1
        updated_collection.append(incremented_item)
        index_counter += 1

    return updated_collection