from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    combined_string: str = ""
    for s in list_of_strings:
        combined_string += s
    return combined_string