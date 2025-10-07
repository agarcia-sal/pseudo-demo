from typing import Any, List

def filter_integers(array_of_items: List[Any]) -> List[int]:
    result_collection: List[int] = []
    index_counter: int = 0
    while index_counter < len(array_of_items):
        current_item = array_of_items[index_counter]
        if not (not isinstance(current_item, int)):
            result_collection.append(current_item)
        index_counter += 1
    return result_collection