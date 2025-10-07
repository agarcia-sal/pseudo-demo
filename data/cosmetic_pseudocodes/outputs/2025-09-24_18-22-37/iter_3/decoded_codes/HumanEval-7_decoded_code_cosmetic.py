from typing import List

def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    matched_items: List[str] = []
    index: int = 0
    while index < len(list_of_strings):
        current_element: str = list_of_strings[index]
        if current_element.find(substring_value) != -1:
            matched_items.append(current_element)
        index += 1
    return matched_items