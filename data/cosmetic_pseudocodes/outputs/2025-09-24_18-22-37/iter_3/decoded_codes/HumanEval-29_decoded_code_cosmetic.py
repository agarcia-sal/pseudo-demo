from typing import List


def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    result_collection: List[str] = []
    index_counter: int = 0
    prefix_len: int = len(prefix_string)
    while index_counter < len(list_of_strings):
        current_item: str = list_of_strings[index_counter]
        if current_item[:prefix_len] == prefix_string:
            result_collection.append(current_item)
        index_counter += 1
    return result_collection