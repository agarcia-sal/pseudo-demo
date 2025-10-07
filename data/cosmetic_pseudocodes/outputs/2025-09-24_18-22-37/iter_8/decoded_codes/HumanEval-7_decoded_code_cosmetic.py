from typing import List

def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    filtered_results: List[str] = []
    idx: int = 0
    while idx < len(list_of_strings):
        current_item: str = list_of_strings[idx]
        if substring_value in current_item:
            filtered_results.append(current_item)
        idx += 1
    return filtered_results