from typing import List

def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    filtered_results: List[str] = []
    for each_element in list_of_strings:
        if substring_value in each_element:
            filtered_results.append(each_element)
    return filtered_results