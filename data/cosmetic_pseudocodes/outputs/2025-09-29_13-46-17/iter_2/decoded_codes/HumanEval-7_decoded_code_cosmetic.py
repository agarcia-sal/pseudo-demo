from typing import List

def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    def helper(input_list: List[str], result_list: List[str]) -> List[str]:
        if not input_list:
            return result_list
        head_element, *tail_elements = input_list
        if substring_value in head_element:
            result_list.append(head_element)
        return helper(tail_elements, result_list)

    return helper(list_of_strings, [])