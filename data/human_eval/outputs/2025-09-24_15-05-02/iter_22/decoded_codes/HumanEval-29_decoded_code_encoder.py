from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    filtered_list: List[str] = []
    for string in list_of_strings:
        if string.startswith(prefix_string):
            filtered_list.append(string)
    return filtered_list