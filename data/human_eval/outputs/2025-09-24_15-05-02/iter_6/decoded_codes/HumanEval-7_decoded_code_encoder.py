from typing import List

def filter_by_substring(list_of_strings: List[str], substring: str) -> List[str]:
    filtered_list = []
    for string_element in list_of_strings:
        if substring in string_element:
            filtered_list.append(string_element)
    return filtered_list