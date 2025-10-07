from typing import List


def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    result: List[str] = []
    for index in range(len(list_of_strings)):
        current_element = list_of_strings[index]
        if current_element.find(substring_value) > 0:
            result.append(current_element)
    return result