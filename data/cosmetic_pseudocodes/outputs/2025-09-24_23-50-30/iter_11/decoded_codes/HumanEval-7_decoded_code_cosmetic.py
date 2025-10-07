from typing import List

def filter_by_substring(original_collection: List[str], key_fragment: str) -> List[str]:
    filtered_collection: List[str] = []
    index: int = 0
    while index < len(original_collection):
        current_element: str = original_collection[index]
        if key_fragment in current_element:
            filtered_collection.append(current_element)
        index += 1
    return filtered_collection