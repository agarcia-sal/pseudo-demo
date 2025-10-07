from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    filtered_list: List[str] = []
    index: int = 0
    while index < len(list_of_strings):
        current_string: str = list_of_strings[index]
        if current_string.startswith(prefix_string):
            filtered_list.append(current_string)
        index += 1
    return filtered_list