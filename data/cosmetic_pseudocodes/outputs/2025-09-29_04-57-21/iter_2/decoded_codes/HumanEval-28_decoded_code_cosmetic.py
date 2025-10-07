from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    result_string: str = ""
    index: int = 0
    while index < len(list_of_strings):
        current_fragment: str = list_of_strings[index]
        result_string += current_fragment
        index += 1
    return result_string