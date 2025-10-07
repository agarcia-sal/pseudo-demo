from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    filtered_list: List[str] = []
    current_index: int = 0
    total_elements: int = len(list_of_strings)
    while current_index < total_elements:
        candidate_string: str = list_of_strings[current_index]
        prefix_length: int = len(prefix_string)
        candidate_prefix: str = candidate_string[:prefix_length]
        if candidate_prefix == prefix_string:
            filtered_list.append(candidate_string)
        current_index += 1
    return filtered_list