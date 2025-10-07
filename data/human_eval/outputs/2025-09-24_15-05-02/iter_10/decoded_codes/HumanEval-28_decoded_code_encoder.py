from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    result = ""
    for string_element in list_of_strings:
        result += string_element
    return result