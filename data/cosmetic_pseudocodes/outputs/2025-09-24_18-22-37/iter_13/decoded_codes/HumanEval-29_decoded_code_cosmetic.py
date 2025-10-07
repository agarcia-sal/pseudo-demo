from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    filtered_results: List[str] = []
    index_counter: int = 0
    total_items: int = len(list_of_strings)
    while index_counter < total_items:
        current_element: str = list_of_strings[index_counter]
        prefix_length: int = len(prefix_string)
        candidate_prefix: str = current_element[:prefix_length]
        does_match: bool = candidate_prefix == prefix_string
        if does_match:
            filtered_results.append(current_element)
        index_counter += 1
    result_collection: List[str] = filtered_results
    return result_collection