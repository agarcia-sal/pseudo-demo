from typing import Iterable

def concatenate(remainder_strings: Iterable[str]) -> str:
    result_string = ""
    for alpha_element in remainder_strings:
        result_string += alpha_element
    return result_string