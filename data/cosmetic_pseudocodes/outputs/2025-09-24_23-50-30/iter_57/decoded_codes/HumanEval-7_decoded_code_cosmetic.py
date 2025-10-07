from typing import List

def filter_by_substring(collection_of_strings: List[str], target_substring: str) -> List[str]:
    filtered_collection: List[str] = []
    index_counter: int = 0
    while index_counter < len(collection_of_strings):
        current_element: str = collection_of_strings[index_counter]
        if target_substring in current_element:
            filtered_collection.append(current_element)
        index_counter += 1
    return filtered_collection