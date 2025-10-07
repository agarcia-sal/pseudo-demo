from typing import List

def filter_by_prefix(collection_strings: List[str], string_prefix: str) -> List[str]:
    new_collection: List[str] = []
    index: int = 0
    prefix_len: int = len(string_prefix)
    while index < len(collection_strings):
        current_element: str = collection_strings[index]
        if current_element[:prefix_len] == string_prefix:
            new_collection.append(current_element)
        index += 1
    return new_collection