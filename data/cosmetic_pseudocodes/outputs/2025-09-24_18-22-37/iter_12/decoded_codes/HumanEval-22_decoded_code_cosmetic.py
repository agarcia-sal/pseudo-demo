from typing import List, Any

def filter_integers(array_of_items: List[Any]) -> List[int]:
    result_collection: List[int] = []
    for index in range(len(array_of_items)):
        current_element = array_of_items[index]
        if isinstance(current_element, int):
            result_collection.append(current_element)
    return result_collection