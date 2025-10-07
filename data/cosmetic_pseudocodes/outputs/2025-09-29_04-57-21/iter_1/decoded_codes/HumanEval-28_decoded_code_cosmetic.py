from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    result: str = ""
    for item in list_of_strings:
        result += item
    return result