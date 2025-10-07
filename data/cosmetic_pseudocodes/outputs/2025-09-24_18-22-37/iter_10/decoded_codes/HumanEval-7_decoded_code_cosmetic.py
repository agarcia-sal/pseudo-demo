from typing import List

def filter_by_substring(array_of_items: List[str], pattern: str) -> List[str]:
    filtered_collection: List[str] = []
    idx: int = 0
    while idx < len(array_of_items):
        current_element: str = array_of_items[idx]
        if pattern in current_element:
            filtered_collection.append(current_element)
        idx += 1
    return filtered_collection