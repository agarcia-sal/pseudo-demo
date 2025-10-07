from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    if not isinstance(list_of_strings, list):
        raise TypeError("list_of_strings must be a list of strings")
    if not isinstance(prefix_string, str):
        raise TypeError("prefix_string must be a string")
    filtered_list: List[str] = []
    for x in list_of_strings:
        if isinstance(x, str) and x.startswith(prefix_string):
            filtered_list.append(x)
    return filtered_list