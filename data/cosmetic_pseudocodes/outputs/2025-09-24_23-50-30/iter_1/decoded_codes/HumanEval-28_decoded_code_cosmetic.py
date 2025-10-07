from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    result: str = ""
    for string in list_of_strings:
        result += string
    return result