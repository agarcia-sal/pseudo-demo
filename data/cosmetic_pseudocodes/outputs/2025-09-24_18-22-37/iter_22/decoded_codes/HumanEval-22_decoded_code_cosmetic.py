from typing import Iterable, List, Union

def filter_integers(collection_of_items: Iterable[object]) -> List[int]:
    filtered_elements: List[int] = []
    index_counter: int = 0
    collection_list = list(collection_of_items)  # Ensure indexing capability
    while index_counter < len(collection_list):
        current_item = collection_list[index_counter]
        if not (not isinstance(current_item, int)):
            filtered_elements.append(current_item)
        index_counter += 1
    return filtered_elements