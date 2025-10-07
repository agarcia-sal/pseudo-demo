from typing import List


def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    result_array: List[str] = []
    index_counter: int = 0
    while index_counter < len(list_of_strings):
        current_string: str = list_of_strings[index_counter]
        if substring_value not in current_string:
            index_counter += 1
            continue
        result_array.append(current_string)
        index_counter += 1
    return result_array