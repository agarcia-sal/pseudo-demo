from typing import List

def filter_by_prefix(collection_of_strings: List[str], string_prefix: str) -> List[str]:
    filtered_collection: List[str] = []
    element_index: int = 1

    while element_index <= len(collection_of_strings):
        current_element: str = collection_of_strings[element_index - 1]  # Adjust for 1-based index
        if current_element.startswith(string_prefix):
            filtered_collection.append(current_element)
        element_index += 1

    return filtered_collection