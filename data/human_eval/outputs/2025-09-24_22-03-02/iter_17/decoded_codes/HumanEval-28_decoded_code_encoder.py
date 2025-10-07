from typing import List

def concatenate(strings: List[str]) -> str:
    result = ""
    for string_element in strings:
        result += string_element
    return result