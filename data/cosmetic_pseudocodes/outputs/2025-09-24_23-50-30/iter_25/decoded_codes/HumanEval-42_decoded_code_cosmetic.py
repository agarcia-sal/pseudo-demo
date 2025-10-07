from typing import Iterable, List, Union

def incr_list(collection_of_items: Iterable[Union[int, float]]) -> List[Union[int, float]]:
    result_collection: List[Union[int, float]] = []
    index_counter: int = 0
    items = list(collection_of_items)  # To support indexing and multiple traversals
    while index_counter < len(items):
        current_item = items[index_counter]
        incremented_item = 1 + current_item
        result_collection.append(incremented_item)
        index_counter += 1
    return result_collection