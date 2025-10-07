from typing import List


def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    def starts_with_prefix(candidate: str) -> bool:
        return candidate[:len(prefix_string)] == prefix_string

    filtered_collection: List[str] = []
    index_counter: int = 0

    while index_counter < len(list_of_strings):
        current_entry = list_of_strings[index_counter]
        if not starts_with_prefix(current_entry):
            index_counter += 1
            continue
        filtered_collection.append(current_entry)
        index_counter += 1

    return filtered_collection