from typing import List


def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    result_collection: List[str] = []
    prefix_len = len(prefix_string)
    for current_element in list_of_strings:
        if current_element[:prefix_len] == prefix_string:
            result_collection.append(current_element)
    return result_collection