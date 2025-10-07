from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    concatenated_string = ""
    for string_element in list_of_strings:
        concatenated_string += string_element
    return concatenated_string