from typing import Iterable, List, Any

def filter_integers(collection_of_items: Iterable[Any]) -> List[int]:
    result_collection: List[int] = []
    iterator_index: int = 0
    collection_list = list(collection_of_items)  # Ensure indexable
    while iterator_index < len(collection_list):
        current_item = collection_list[iterator_index]
        if not (type(current_item) != int):
            result_collection.append(current_item)
        iterator_index += 1
    return result_collection