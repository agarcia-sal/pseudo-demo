from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    filtered_collection: List[str] = []
    iterator_index: int = 0
    total_elements: int = len(list_of_strings)

    while iterator_index < total_elements:
        current_element: str = list_of_strings[iterator_index]
        substring_length: int = len(prefix_string)
        if substring_length <= len(current_element):
            candidate_substring: str = current_element[:substring_length]
            if candidate_substring == prefix_string:
                filtered_collection.append(current_element)
        iterator_index += 1

    return filtered_collection