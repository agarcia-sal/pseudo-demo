from typing import List

def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    result_collection: List[str] = []
    iterator_position: int = 0
    while iterator_position < len(list_of_strings):
        candidate_string: str = list_of_strings[iterator_position]
        if candidate_string.find(substring_value) != -1:
            result_collection.append(candidate_string)
        iterator_position += 1
    return result_collection