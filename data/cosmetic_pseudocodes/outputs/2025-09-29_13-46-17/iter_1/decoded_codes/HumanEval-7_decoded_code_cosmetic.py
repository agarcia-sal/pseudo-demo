from typing import List

def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    filtered_list: List[str] = [element for element in list_of_strings if substring_value in element]
    return filtered_list