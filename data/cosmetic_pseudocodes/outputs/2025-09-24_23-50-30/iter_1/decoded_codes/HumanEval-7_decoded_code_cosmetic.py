from typing import List

def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    filtered_results: List[str] = []
    for element in list_of_strings:
        if substring_value in element:
            filtered_results.append(element)
    return filtered_results