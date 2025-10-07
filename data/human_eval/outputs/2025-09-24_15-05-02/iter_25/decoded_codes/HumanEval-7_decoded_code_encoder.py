from typing import List

def filter_by_substring(list_of_strings: List[str], substring: str) -> List[str]:
    filtered_list: List[str] = [string_element for string_element in list_of_strings if substring in string_element]
    return filtered_list