from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    filtered_collection: List[str] = []
    index: int = 0
    length_of_list: int = len(list_of_strings)
    while index < length_of_list:
        current_element: str = list_of_strings[index]
        if current_element[:len(prefix_string)] == prefix_string:
            filtered_collection.append(current_element)
        index += 1
    return filtered_collection