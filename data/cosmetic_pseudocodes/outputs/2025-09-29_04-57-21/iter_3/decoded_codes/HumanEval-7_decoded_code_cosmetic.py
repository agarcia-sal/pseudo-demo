from typing import List


def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    result_list: List[str] = []
    for text_element in list_of_strings:
        if substring_value in text_element:
            result_list.append(text_element)
    return result_list