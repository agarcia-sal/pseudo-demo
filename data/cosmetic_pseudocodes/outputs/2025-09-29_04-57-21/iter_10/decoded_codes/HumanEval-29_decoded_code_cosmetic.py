from typing import List


def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    filtered_results: List[str] = []
    index_counter: int = 0
    while index_counter < len(list_of_strings):
        current_candidate = list_of_strings[index_counter]
        if current_candidate[:len(prefix_string)] == prefix_string:
            filtered_results.append(current_candidate)
        index_counter += 1
    return filtered_results