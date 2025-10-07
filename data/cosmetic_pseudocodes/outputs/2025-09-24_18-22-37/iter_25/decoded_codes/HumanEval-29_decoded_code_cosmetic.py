from typing import List


def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    filtered_collection: List[str] = []
    idx: int = 0
    total_count: int = len(list_of_strings)

    while idx < total_count:
        current_candidate: str = list_of_strings[idx]
        prefix_len: int = len(prefix_string)

        if current_candidate[:prefix_len] == prefix_string:
            filtered_collection.append(current_candidate)

        idx += 1

    return filtered_collection