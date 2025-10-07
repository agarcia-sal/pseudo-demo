from typing import List


def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    filtered_list: List[str] = []
    iterator_index: int = 0
    while iterator_index < len(list_of_strings):
        current_element: str = list_of_strings[iterator_index]
        if not current_element.startswith(prefix_string):
            iterator_index += 1
            continue
        filtered_list.append(current_element)
        iterator_index += 1
    return filtered_list