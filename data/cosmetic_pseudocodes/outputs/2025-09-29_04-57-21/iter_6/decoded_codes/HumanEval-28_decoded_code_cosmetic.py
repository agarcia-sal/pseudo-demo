from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    result_string: str = ""
    for individual_string in list_of_strings:
        result_string += individual_string
    return result_string