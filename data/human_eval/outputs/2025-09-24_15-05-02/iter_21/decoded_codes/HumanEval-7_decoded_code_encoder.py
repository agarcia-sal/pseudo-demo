from typing import List

def filter_by_substring(list_of_strings: List[str], substring: str) -> List[str]:
    filtered_list: List[str] = []
    for string in list_of_strings:
        if substring in string:
            filtered_list.append(string)
    return filtered_list