from typing import List, Any

def filter_integers(collection_of_items: List[Any]) -> List[int]:
    filtered_elements: List[int] = []
    iterator_index: int = 0

    while iterator_index < len(collection_of_items):
        current_entry = collection_of_items[iterator_index]
        if isinstance(current_entry, int):
            filtered_elements.append(current_entry)
        iterator_index += 1

    return filtered_elements