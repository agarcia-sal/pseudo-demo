from typing import List

def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    filtered_strings: List[str] = []
    element_index: int = 0
    while element_index < len(list_of_strings):
        current_string: str = list_of_strings[element_index]
        found_index: int = current_string.find(substring_value)
        if found_index != -1:
            filtered_strings.append(current_string)
        element_index += 1
    return filtered_strings