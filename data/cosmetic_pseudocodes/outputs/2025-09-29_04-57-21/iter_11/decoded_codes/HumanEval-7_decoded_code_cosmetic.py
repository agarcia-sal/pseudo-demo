from typing import List

def filter_by_substring(string_collection: List[str], sub_value: str) -> List[str]:
    filtered_results: List[str] = []
    iterator_index: int = 0
    while iterator_index < len(string_collection):
        current_entry: str = string_collection[iterator_index]
        if sub_value in current_entry:
            filtered_results.append(current_entry)
        iterator_index += 1
    return filtered_results