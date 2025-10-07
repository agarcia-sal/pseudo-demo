from typing import List


def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    filtered_collection: List[str] = []
    position: int = 0
    while position < len(list_of_strings):
        current_element: str = list_of_strings[position]
        if not current_element.startswith(prefix_string):
            position += 1
            continue
        filtered_collection.append(current_element)
        position += 1
    return filtered_collection