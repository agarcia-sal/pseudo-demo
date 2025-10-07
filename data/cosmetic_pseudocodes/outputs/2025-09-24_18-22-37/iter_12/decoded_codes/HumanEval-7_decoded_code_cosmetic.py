from typing import List


def filter_by_substring(collection_of_items: List[str], target_fragment: str) -> List[str]:
    result_collection: List[str] = []
    idx: int = 0
    while idx < len(collection_of_items):
        current_element: str = collection_of_items[idx]
        contains_fragment: bool = False
        if target_fragment in current_element:
            contains_fragment = True
        if contains_fragment:
            result_collection.append(current_element)
        idx += 1
    return result_collection