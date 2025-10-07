from typing import List


def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    filtered_items: List[str] = []
    index: int = len(list_of_strings) - 1
    while index >= 0:
        if not (substring_value not in list_of_strings[index]):
            filtered_items.append(list_of_strings[index])
        index -= 1
    return list(reversed(filtered_items))