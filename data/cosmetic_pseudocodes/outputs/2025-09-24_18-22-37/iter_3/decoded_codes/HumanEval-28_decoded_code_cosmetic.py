from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    result: str = ""
    index: int = 0
    while index < len(list_of_strings):
        result += list_of_strings[index]
        index += 1
    return result