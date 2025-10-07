from typing import Iterable, List, Union

def filter_integers(collection_of_items: Iterable[object]) -> List[int]:
    filtered_collection: List[int] = []
    iterator: int = 0
    collection_list = list(collection_of_items)  # to use indexing safely
    while iterator < len(collection_list):
        current_item = collection_list[iterator]
        if isinstance(current_item, int):
            filtered_collection.append(current_item)
        iterator += 1
    return filtered_collection