from typing import List


def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    filtered_collection: List[str] = []
    iterator_index: int = 0

    while iterator_index < len(list_of_strings):
        candidate_string: str = list_of_strings[iterator_index]

        if substring_value not in candidate_string:
            iterator_index += 1
            continue

        filtered_collection.append(candidate_string)
        iterator_index += 1

    return filtered_collection